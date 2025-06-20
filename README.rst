sphinxcontrib-twine
###################

|pylint-action| |test-action| |pypi-action|

|pypi-version| |pypi-python|  |pypi-status|

|docs-badge|


Add some interactive stories (`Twine`_) in your Sphinx docs.


Features
********

- Story formats: `Chapbook`_, `Harlowe`_, `Snowman`_, `SugarCube`_
- Contains multiple `Twine`_ stories in one page
- All *format.js* files are imported from `twinejs`_ and `cdn.jsdelivr.net <https://github.com/jixingcn/sphinxcontrib-twine/tree/main/sphinxcontrib/twine/storyformats.json>`_


Use
***

::

    $ pip install sphinxcontrib-twine

::

    extensions = [
        ...,
        'sphinxcontrib.twine'
    ]

::

    .. twine::
        :format: Chapbook
        :title: Test
        :width: 100%
        :height: 500
    
        :: StoryTitle
        Test in Chapbook
    
        :: Start
        Start


License
*******

|license|



.. |pylint-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pylint.yml?label=pylint
    :alt: pylint workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/pylint.yml


.. |test-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/test.yml?label=test
    :alt: test workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/test.yml


.. |pypi-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pypi.yml?label=pypi
    :alt: pypi workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/pypi.yml


.. |pypi-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-twine
    :alt: PyPI - Version
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |pypi-python| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-twine
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |pypi-status| image:: https://img.shields.io/pypi/status/sphinxcontrib-twine
    :alt: PyPI - Status
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |docs-badge| image:: https://img.shields.io/readthedocs/sphinxcontrib-twine/latest
    :alt: Read the Docs (version)
    :target: https://sphinxcontrib-twine.readthedocs.io


.. |license| image:: https://img.shields.io/badge/license-MIT-green
    :alt: Static Badge
    :target: https://github.com/jixingcn/sphinxcontrib-twine/blob/main/LICENSE


.. _Twine: https://twinery.org/


.. _Chapbook: https://klembot.github.io/chapbook/


.. _Harlowe: https://twine2.neocities.org/


.. _Snowman: https://videlais.github.io/snowman/


.. _SugarCube: https://www.motoslave.net/sugarcube/2/


.. _twinejs: https://github.com/klembot/twinejs
