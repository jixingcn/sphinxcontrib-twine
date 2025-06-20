'''
Add some twine stories in Sphinx docs.
'''
# -*- coding: utf-8 -*-

# pylint: disable=too-few-public-methods

import sphinx
import docutils

from . import twine


__title__   = 'sphinxcontrib-twine'
__version__ = '0.3.2'
__authors__ = [{'name': 'Xing Ji', 'email': 'me@xingji.me'}]


def setup(app: sphinx.application.Sphinx):
    '''
    Setup when Sphinx calls this extension.
    '''

    twine.setup(app)

    return {
        'version'             : __version__,
        'env_version'         : 1,
        'parallel_read_safe'  : True,
        'parallel_write_safe' : True,
    }
