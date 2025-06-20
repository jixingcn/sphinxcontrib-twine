'''
Sphinx docs configuration
'''
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pylint: disable=invalid-name

import datetime
import sys
import os


docs_path    = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(docs_path)

# use the project
sys.path.insert(0, project_path)

from sphinxcontrib import twine # pylint: disable=wrong-import-position, no-name-in-module

project   = twine.__title__
version   = twine.__version__
authors   = ','.join([f'{author["name"]} ({author["email"]})' for author in twine.__authors__])
copyright = f'{datetime.datetime.now().year}, {authors}.' # pylint: disable=redefined-builtin


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    #'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx_rtd_theme',
    'sphinx_rtd_dark_mode',
    'sphinxcontrib.twine',
]

html_theme           = 'sphinx_rtd_theme' # pylint: disable=invalid-name
#html_static_path     = ['_static']
html_extra_path      = []
#html_favicon         = '_static/favicon.png'
#html_logo            = '_static/favicon.png'
html_copy_source     = False # pylint: disable=invalid-name
html_show_sourcelink = False # pylint: disable=invalid-name
html_css_files       = []
html_js_files        = []

exclude_patterns = []
source_suffix    = {'.rst': 'restructuredtext'}
master_doc       = 'index' # pylint: disable=invalid-name

gettext_compact = False # pylint: disable=invalid-name
pygments_style  = 'default' # pylint: disable=invalid-name
