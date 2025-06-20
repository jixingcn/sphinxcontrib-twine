'''
Load story formats from local directory
'''
# pylint: disable=invalid-name, redefined-outer-name

import os
import re
import json


STORY_FORMATS = {}

TWINE_ROOT_DIRPATH    = os.path.dirname(__file__)
RE_NAME_VERSION       = re.compile(
r'^(?P<name>[0-9a-zA-Z]+)-'
r'(?P<major>[0-9]+).'
r'(?P<minor>[0-9]+).'
r'(?P<patch>[0-9]+)$')


def collect_formats():
    '''
    Collect all formats form local directory
    '''

    with open(os.path.join(TWINE_ROOT_DIRPATH, 'storyformats.json'), 'rt', encoding='utf-8') as f:
        formats_config = json.loads(f.read())

        for story_format, story_format_ctx in formats_config.items():
            story_format_new = {}
            for format_version_str, format_version_ctx in story_format_ctx.items():
                format_version = tuple(int(v) for v in format_version_str.split('.'))
                story_format_new[format_version] = format_version_ctx
            STORY_FORMATS[story_format] = story_format_new

collect_formats()


def get_valid_format(story_format, format_version=None):
    '''
    Get the format information by format and version
    '''
    story_format = story_format.lower()
    if story_format not in STORY_FORMATS:
        raise ValueError(f'No valid format - {story_format}')
    valid_story_format = STORY_FORMATS[story_format]

    if format_version is not None:
        format_version = tuple(int(v) for v in format_version.split('.'))
        if len(format_version) < 3:
            format_version = list(format_version)
            for _ in range(len(format_version), 3):
                format_version.append(0)
            format_version = tuple(format_version)

        if format_version in valid_story_format:
            return valid_story_format[format_version]
    elif len(valid_story_format) > 0:
        valid_story_format_versions = list(valid_story_format.keys())
        valid_story_format_versions.sort(reverse=True)
        return valid_story_format[valid_story_format_versions[0]]

    raise ValueError(f'No valid format - {story_format} v{format_version}')
