'''
Add some twine stories in Sphinx docs.
'''
# -*- coding: utf-8 -*-

import sphinx
import docutils

import pytwee


__title__   = 'sphinxcontrib-twine'
__version__ = '0.3.0'
__authors__ = [{'name': 'Xing Ji', 'email': 'me@xingji.me'}]


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

        story  = pytwee.Story()

        parser = pytwee.twee3.Parser(story)
        for line in self.content:
            parser(line)
        del parser

        if 'title' in self.options:
            title = self.options['title'].strip()
            if title != '':
                story.title = title

        twine2html = []
        unparser   = pytwee.twee2.UnparserHTML(story)
        for line in iter(unparser, None):
            twine2html.append(line)

        node['compiled'] = '\n'.join(twine2html)
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
