Usage
#####

Configure
*********

::

    # Install from pypi
    $ pip install sphinxcontrib-twine

::

    # Insert the externsion in sphinx' conf.py
    extensions = [
        ...,
        'sphinxcontrib.twine'
    ]


Directive
*********

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

**Options:**

* **format**: *string* One of Chapbook, Harlowe, Snowman, SugarCube
* **title**: *string* Set the title for your story
* **width**: *string* The width style for story's *iframe*
* **height**: *string* The height style for story's *iframe*
