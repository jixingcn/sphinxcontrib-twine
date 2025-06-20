'''
Add some twine stories in Sphinx docs.
'''
# -*- coding: utf-8 -*-

# pylint: disable=too-few-public-methods

import os
import urllib

import html
import sphinx
import docutils

import pytwee
import jinja2

from . import storyformats


class Node(docutils.nodes.General, docutils.nodes.Inline, docutils.nodes.Element):
    '''
    The doctree node for twine.
    '''
    def __init__(self, src_dir, relative_path, **options):
        super().__init__()

        self.src_dir       = src_dir
        self.relative_path = relative_path
        self.options       = options


def html_visit(self, node):
    '''
    Generate the html element by the node.
    '''
    story = node['story']

    iframe_attributes = {}
    iframe_attributes['width']  = node.options['width'] if 'width' in node.options else '100%'
    iframe_attributes['height'] = node.options['height'] if 'height' in node.options else '500'
    iframe_attributes['style']  = 'margin: 0; padding: 0; border: 0; overflow: hidden;'

    twine2script    = _html_visit_twine2script(node, story)
    twine2storydata = _html_visit_twine2storydata(story)

    twine2story_dirpath  = os.path.dirname(__file__)
    twine2story_filepath = os.path.join(twine2story_dirpath, 'twine2story.html')
    twine2story_template = None
    with open(twine2story_filepath, 'rt', encoding='utf-8') as f:
        twine2story_template = ''.join(f.readlines())
    twine2story_template = jinja2.Template(twine2story_template)
    iframe_attributes['srcdoc'] = html.escape(twine2story_template.render(
        twine2script    = twine2script,
        twine2storydata = twine2storydata,
        ))

    iframe_attributes = ' '.join([f'{k}="{v}"' for k, v in iframe_attributes.items()])

    self.body.append(f'<iframe {iframe_attributes}></iframe>')
    raise docutils.nodes.SkipNode

def _html_visit_twine2script(node, story):
    story_format         = story.data['format']
    story_format_version = None
    if 'format-version' in story.data:
        story_format_version = story.data['format-version']
    valid_format = storyformats.get_valid_format(story_format, format_version=story_format_version)
    if 'format.js' not in valid_format:
        raise ValueError(f'No format.js in {valid_format}!')
    format_js     = valid_format['format.js']

    format_js_url = urllib.parse.urlparse(format_js)
    if format_js_url.scheme == '':
        relative_path = './' + os.path.dirname(node.relative_path)
        relative_path = os.path.relpath('.', relative_path)
        format_js = relative_path + '/_static/' + format_js

    twine2script = f'<script type="module" src="{format_js}"></script>'
    return twine2script

def _html_visit_twine2storydata(story):
    twine2html = []
    unparser   = pytwee.twee2.UnparserHTML(story)
    for line in iter(unparser, None):
        twine2html.append(line)
    twine2storydata = '\n'.join(twine2html)
    return twine2storydata


class Directive(sphinx.util.docutils.SphinxDirective):
    '''
    The Sphinx directive for the twine chapbook
    '''

    has_content               = True
    final_argument_whitespace = False
    option_spec               = {
        'ifid':           sphinx.util.docutils.directives.unchanged,
        'format':         sphinx.util.docutils.directives.unchanged,
        'format-version': sphinx.util.docutils.directives.unchanged,
        'title':          sphinx.util.docutils.directives.unchanged,
        'width':          sphinx.util.docutils.directives.unchanged,
        'height':         sphinx.util.docutils.directives.unchanged,
    }

    def run(self, *args, **kwargs): # pylint: disable=unused-argument
        '''
        Process the twine-chapbook directive
        '''
        relative_path = os.path.relpath(self.get_source_info()[0], self.env.srcdir)
        node          = Node(self.env.srcdir, relative_path, **self.options)

        story  = pytwee.Story()

        parser = pytwee.twee3.Parser(story)
        for line in self.content:
            parser(line)
        del parser

        if 'ifid' in self.options:
            story_ifid = self.options['ifid'].strip()
            story.data['ifid'] = story_ifid

        if 'format' in self.options:
            story_format = self.options['format'].strip()
            story.data['format'] = story_format

        if 'format-version' in self.options:
            story_format_version = self.options['format-version'].strip()
            story.data['format-version'] = story_format_version

        if 'title' in self.options:
            title = self.options['title'].strip()
            if title != '':
                story.title = title

        node['story'] = story
        self.add_name(node)
        return [node]


def setup(app: sphinx.application.Sphinx):
    '''
    Setup when Sphinx calls this extension.
    '''

    app.add_node(
        Node,
        html = (html_visit, None),
    )
    app.add_directive('twine', Directive)
