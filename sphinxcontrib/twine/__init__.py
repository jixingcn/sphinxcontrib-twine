'''
Add some twine stories in Sphinx docs.
'''
# -*- coding: utf-8 -*-

import sphinx
import docutils

__title__       = 'sphinxcontrib-twine'
__description__ = 'sphinxcontrib-twine'
__version__     = '0.2.0'


class TwineChapbookNode(docutils.nodes.General, docutils.nodes.Inline, docutils.nodes.Element):
    '''
    The doctree node for twine chapbook.
    '''
    def __init__(self, **options):
        super().__init__()

        self.options = options


def html_visit_twine_chapbook(self, node):
    '''
    Generate the html element by the node.
    '''
    iframe_attributes           = {}
    iframe_attributes['width']  = node.options['width'] if 'width' in node.options else '100%'
    iframe_attributes['height'] = node.options['height'] if 'height' in node.options else '500'
    iframe_attributes           = [f'{k}="{v}"' for k, v in iframe_attributes.items()]
    iframe_attributes           = ' '.join(iframe_attributes)

    self.body.append('<div class="twine_chapbook">')
    self.body.append(f'<iframe {iframe_attributes}></iframe>')
    if 'code' in node:
        twine_chapbook_code = node['code']
        self.body.append(f'<pre>{twine_chapbook_code}</pre>')

    twine_chapbook_compiled = node['compiled']

    self.body.append(f'<div hidden>{twine_chapbook_compiled}</div>')
    self.body.append('</div>')
    raise docutils.nodes.SkipNode


class StoryData: # pylint: disable=too-few-public-methods
    '''
    The data about the twine story.

    * Parse the twine file format
    * Convert to HTML
    '''

    def __init__(self, name: str = None, startnode: int = None):
        self.name      = name
        self.startnode = startnode
        self.passages  = []

    def html(self):
        '''
        Generate the HTML format by the context of the data.
        '''

        title = self.name
        if title is None:
            title = ''

        # find a valid `startnode`
        startnode = None
        for i, passage in enumerate(self.passages):
            # default is first passage
            if startnode is None:
                startnode = i
            if passage.name == self.startnode:
                startnode = i
                break
        if startnode is None:
            raise ValueError(f'can\'t find startnode - {self.startnode}')

        html_code = f'<tw-storydata name="{title}" startnode="{startnode}">'

        for i, passage in enumerate(self.passages):
            passage    = self.passages[i]
            html_code += passage.html(i)

        html_code += '</tw-storydata>'
        return html_code


class StorySegment: # pylint: disable=too-few-public-methods
    '''
    Basic class of the story segment.
    '''

    def __init__(self, data):
        self.data = data

    def __call__(self, line):
        pass


class StorySegmentStoryTitle(StorySegment): # pylint: disable=too-few-public-methods
    '''
    Use the `StoryTitle` segment to set the title.
    '''

    id = 'StoryTitle'

    def __call__(self, line):
        line = line.strip()
        if line == '':
            return

        self.data.name = line


class StorySegmentStoryData(StorySegment): # pylint: disable=too-few-public-methods
    '''
    Use the `StoryData` segment to set the startnode(index) and title.
    '''

    id = 'StoryData'

    def __call__(self, line):
        line = line.strip()
        if line == '':
            return

        line_segs = line.split(':')
        if len(line_segs) != 2:
            return

        line_key, line_value = line.split(':')
        line_key             = line_key.strip().lower()
        line_value           = line_value.strip()

        if line_key == 'index':
            self.data.startnode = line_value
        elif line_key == 'title' and line_value != '':
            self.data.name = line_value


class StorySegmentPassage(StorySegment):
    '''
    Process the passage segment
    '''

    def __init__(self, data, name):
        super().__init__(data)

        self.name  = name
        self.lines = []

        data.passages.append(self)

    def __call__(self, line):
        self.lines.append(line)

    def html(self, pid):
        '''
        Genearte this passage to HTML
        '''

        html_lines = []
        html_lines.append(f'<tw-passagedata name="{self.name}" pid="{pid}">')
        html_lines.append('\n'.join(self.lines))
        html_lines.append('</tw-passagedata>')

        return '\n'.join(html_lines)


class TwineChapbook(sphinx.util.docutils.SphinxDirective):
    '''
    The Sphinx directive for the twine chapbook
    '''

    has_content               = True
    final_argument_whitespace = False
    option_spec               = {
        'title':  sphinx.util.docutils.directives.unchanged,
        'width':  sphinx.util.docutils.directives.unchanged,
        'height': sphinx.util.docutils.directives.unchanged,
    }

    def run(self, *args, **kwargs): # pylint: disable=unused-argument
        node = TwineChapbookNode(**self.options)

        story_data    = StoryData()
        story_segment = None
        for line in self.content:
            if line.startswith('::'):
                story_tag = line[2:].strip()
                if line[2:].strip() == StorySegmentStoryTitle.id:
                    story_segment = StorySegmentStoryTitle(story_data)
                elif line[2:].strip() == StorySegmentStoryData.id:
                    story_segment = StorySegmentStoryData(story_data)
                else:
                    story_segment = StorySegmentPassage(story_data, story_tag)
            elif story_segment is not None:
                story_segment(line)

        if 'title' in self.options:
            title = self.options['title'].strip()
            if title != '':
                story_data.name = title

        node['compiled'] = story_data.html()
        self.add_name(node)
        return [node]


def on_html_page_context(app: sphinx.application.Sphinx,
                         pagename,     # pylint: disable=unused-argument
                         templatename, # pylint: disable=unused-argument
                         context,      # pylint: disable=unused-argument
                         doctree):
    '''
    Add some scripts to activating the twine chapbook when the doctree contains the twine chapbook.
    '''

    if doctree and not doctree.next_node(TwineChapbookNode):
        return

    js_body = '''
window.storyFormat = function (data) {
    const all_twine_chapbook_elems = document.querySelectorAll(".twine_chapbook");
    all_twine_chapbook_elems.forEach((elem) => {
      var twine_chapbook_frame = elem.querySelector("iframe");
      var twine_chapbook_story = elem.querySelector("tw-storydata");
      var twine_chapbook_source = data.source;
      twine_chapbook_source = twine_chapbook_source.replace("{{STORY_NAME}}", twine_chapbook_story.getAttribute("name"));
      twine_chapbook_source = twine_chapbook_source.replace("{{STORY_DATA}}", twine_chapbook_story.outerHTML);
      twine_chapbook_frame.srcdoc = twine_chapbook_source;
    });
};
'''
    app.add_js_file(None, body=js_body)
    app.add_js_file("https://klembot.github.io/chapbook/use/2.3.0/format.js", type='module')


def setup(app: sphinx.application.Sphinx):
    '''
    Setup when Sphinx calls this extension.
    '''

    app.add_node(
        TwineChapbookNode,
        html = (html_visit_twine_chapbook, None),
    )
    app.add_directive('twine-chapbook', TwineChapbook)

    app.connect('html-page-context', on_html_page_context)

    return {
        'version'             : __version__,
        'env_version'         : 1,
        'parallel_read_safe'  : True,
        'parallel_write_safe' : True,
    }
