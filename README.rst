sphinxcontrib-twine
###################

|sphinxcontrib-twine-version| |python-versions| |docs-badge| |pylint-badge|


Add some interactive stories (`Twine`_) in your Sphinx docs.


Features
********

- Supports `Chapbook`_


TL;DR
*****

::

    $ pip install sphinxcontrib-twine

::

    extensions = [
        ...,
        'sphinxcontrib.twine'
    ]

::

    .. twine-chapbook::                                :title: Deep Mind
       :width: 100%
       :height: 600


License
*******

Under `MIT License <https://github.com/jixingcn/sphinxcontrib-twine/blob/main/LICENSE>`_.



.. |sphinxcontrib-twine-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |python-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |docs-badge| image:: https://img.shields.io/readthedocs/sphinxcontrib-twine
    :target: https://sphinxcontrib-twine.readthedocs.io


.. |pylint-badge| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pylint.yml?branch=main&label=pylint
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions


.. _Twine: https://twinery.org/


.. _Chapbook: https://klembot.github.io/chapbook/

