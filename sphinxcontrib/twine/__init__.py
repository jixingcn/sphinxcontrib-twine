# -*- coding: utf-8 -*-

import sphinx
import docutils

__title__ = 'sphinxcontrib-twine'
__description__ = 'sphinxcontrib-twine'
__version__ = '0.1.0'


class twine_chapbook(docutils.nodes.General, docutils.nodes.Inline, docutils.nodes.Element):
    def __init__(self, **options):
        super().__init__()

        self.options = options


def html_visit_twine_chapbook(self, node):
    twine_chapbook_compiled = node['compiled']
    iframe_attributes = {}
    iframe_attributes['width'] = node.options['width'] if 'width' in node.options else '100%'
    iframe_attributes['height'] = node.options['height'] if 'height' in node.options else '500'
    iframe_attributes = ' '.join([f'{k}="{iframe_attributes[k]}"' for k in iframe_attributes])
    self.body.append('<div class="twine_chapbook">')
    self.body.append(f'<iframe {iframe_attributes}></iframe>')
    if 'code' in node:
        twine_chapbook_code = node['code']
        self.body.append(f'<pre>{twine_chapbook_code}</pre>')
    self.body.append(f'<div hidden>{twine_chapbook_compiled}</div>')
    self.body.append('</div>')
    raise docutils.nodes.SkipNode


class StoryData:
    def __init__(self):
        self.name = None
        self.startnode = None
        self.passages = []

    def html(self):
        title = self.name
        if title is None:
            title = ''

        startnode = None
        for i in range(len(self.passages)):
            passage = self.passages[i]
            # default is first passage
            if startnode is None:
                startnode = i
            if passage.name == self.startnode:
                startnode = i
                break
        if startnode is None:
            raise Exception(f'can\'t find startnode - {self.startnode}')

        html_code = f'<tw-storydata name="{title}" startnode="{startnode}">'

        for i in range(len(self.passages)):
            passage = self.passages[i]
            html_code += passage.html(i)

        html_code += '</tw-storydata>'
        return html_code


class StorySegment:
    def __init__(self, data):
        self.data = data

    def __call__(self, line):
        pass

class StorySegmentStoryTitle(StorySegment):
    id = 'StoryTitle'

    def __init__(self, data):
        super(StorySegmentStoryTitle, self).__init__(data)

    def __call__(self, line):
        line = line.strip()
        if line == '':
            return

        self.data.name = line

class StorySegmentStoryData(StorySegment):
    id = 'StoryData'

    def __init__(self, data):
        super(StorySegmentStoryData, self).__init__(data)

    def __call__(self, line):
        line = line.strip()
        if line == '':
            return

        line_segs = line.split(':')
        if len(line_segs) != 2:
            return

        line_key, line_value = line.split(':')
        line_key = line_key.strip().lower()
        line_value = line_value.strip()

        if line_key == 'index':
            self.data.startnode = line_value
        elif line_key == 'title' and line_value != '':
            self.data.name = line_value

class StorySegmentPassage(StorySegment):
    def __init__(self, data, name):
        super(StorySegmentPassage, self).__init__(data)

        self.name = name
        self.lines = []

        data.passages.append(self)

    def __call__(self, line):
        self.lines.append(line)

    def html(self, pid):
        html_lines = []
        html_lines.append(f'<tw-passagedata name="{self.name}" pid="{pid}">')
        html_lines.append('\n'.join(self.lines))
        html_lines.append(f'</tw-passagedata>')
        return '\n'.join(html_lines)


class TwineChapbook(sphinx.util.docutils.SphinxDirective):
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        'title':  sphinx.util.docutils.directives.unchanged,
        'width':  sphinx.util.docutils.directives.unchanged,
        'height': sphinx.util.docutils.directives.unchanged,
    }

    def run(self, *args, **kwargs):
        node = twine_chapbook(**self.options)
        story_data = StoryData()
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


def on_html_page_context(app: sphinx.application.Sphinx, pagename, templatename, context, doctree):
    if doctree and not doctree.next_node(twine_chapbook):
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
    app.add_node(
        twine_chapbook,
        html=(html_visit_twine_chapbook, None),
    )
    app.add_directive('twine_chapbook', TwineChapbook)

    app.connect('html-page-context', on_html_page_context)

    return {
        'version': __version__,
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
