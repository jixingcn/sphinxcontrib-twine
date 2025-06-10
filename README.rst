Sphinx Twine Extension
======================

|sphinxcontrib-twine-version| |python-versions| |docs-badge| |pylint-badge|


Add some interactive stories (|Twine|) in your Sphinx docs.


Features
--------

- Supports |Chapbook|


Installation
------------

::

    $ pip install sphinxcontrib-twine


Usage
-----

Configuration
^^^^^^^^^^^^^

Then add ``sphinxcontrib.twine`` in ``extensions`` list of your project's ``conf.py``::

    extensions = [
        ...,
        'sphinxcontrib.twine'
    ]

Directive options
^^^^^^^^^^^^^^^^^



.. |sphinxcontrib-twine-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |python-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |docs-badge| image:: https://img.shields.io/readthedocs/sphinxcontrib-twine
    :target: https://sphinxcontrib-twine.readthedocs.io


.. |pylint-badge| image:: https://img.shields.io/github/actions/workflow/status/jixingcn/sphinxcontrib-twine/pylint.yml?branch=main&label=pylint
    :target: https://github.com/jixingcn/sphinxcontrib-twine/actions


.. |Twine| raw:: html

    <a href="https://twinery.org/" target="_blank">Twine</a>


.. |Chapbook| raw:: html

    <a href="https://klembot.github.io/chapbook/" target="_blank">Chapbook</a>
