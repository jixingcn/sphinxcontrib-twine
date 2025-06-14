sphinxcontrib-twine
###################

|pylint-action| |pypi-action| |test-action|

|docs-badge|

|pypi-version| |pypi-python|  |pypi-status|


Add some interactive stories (`Twine`_) in your Sphinx docs.


Features
********

- Support `Chapbook`_
- [TODO] Support `Harlowe`_
- [TODO] Support `Snowman`_
- [TODO] Support `SugarCube`_


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

    .. twine-chapbook::
       :title: Deep Mind
       :width: 100%
       :height: 600


License
*******

|license|



.. |pylint-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pylint.yml?label=pylint
    :alt: pylint workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/pylint.yml


.. |pypi-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pypi.yml?label=pypi
    :alt: pypi workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/pypi.yml

.. |test-action| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/test.yml?label=test
    :alt: test workflow Status
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions/workflows/test.yml


.. |docs-badge| image:: https://img.shields.io/readthedocs/sphinxcontrib-twine/latest
    :alt: Read the Docs (version)
    :target: https://sphinxcontrib-twine.readthedocs.io


.. |pypi-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-twine
    :alt: PyPI - Version
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |pypi-python| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-twine
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |pypi-status| image:: https://img.shields.io/pypi/status/sphinxcontrib-twine
    :alt: PyPI - Status
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |license| image:: https://img.shields.io/badge/license-MIT-green
    :alt: Static Badge
    :target: https://github.com/jixingcn/sphinxcontrib-twine/blob/main/LICENSE


.. _Twine: https://twinery.org/


.. _Chapbook: https://klembot.github.io/chapbook/


.. _Harlowe: https://twine2.neocities.org/


.. _Snowman: https://videlais.github.io/snowman/


.. _SugarCube: https://www.motoslave.net/sugarcube/2/

