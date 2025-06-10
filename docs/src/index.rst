|sphinxcontrib-twine-version| |python-versions| |docs-badge| |build-badge|

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


Examples
--------

.. twine_chapbook::
    :title: Cloak of Darkness
    :width: 100%
    :height: 500

    :: Start
    room: ''
    hasCloak: true
    config.header.center: '{room}'
    --
    [align center]
    # Cloak of Darkness
    
    {embed unsplash image: 'https://unsplash.com/photos/rF1OwUp065Q'}
    
    _based on work by [[Iain Merrick->http://www.philome.la/iainmerrick/cloak-of-darkness/play]]_  
    _photo by [[Alessia Cocconi->https://unsplash.com/photos/rF1OwUp065Q]]_
    
    **[[Begin->Outside]]**
    
    
    :: Outside
    room: 'Outside'
    --
    Hurrying through the rainswept November night, you're glad to see the bright lights of the [[Opera House->Foyer]]. It's surprising that there aren't more people about but, hey, what do you expect in a cheap demo game...?
    
    
    :: Cloak
    A handsome cloak, of velvet trimmed with satin, and slightly spattered with raindrops. Its blackness is so deep that it almost seems to suck light from the room.
    
    [align center]
    {back link}
    
    
    :: Foyer
    _previousRoom: room
    room: 'Foyer of the Opera House'
    outside: false
    --
    [if _previousRoom === 'Outside']
    Shaking the rain from your [[cloak->Cloak]], you step gratefully inside.
    
    [cont'd]
    You are standing in a spacious hall, splendidly decorated in red and gold, with glittering chandeliers overhead. The entrance from the street is to the [[north->Outside]], and there are doorways [[south->Bar]] and [[west->Cloakroom]].
    
    
    :: Cloakroom
    room: 'Cloakroom'
    --
    The walls of this small room were clearly once lined with hooks, though now [[only one remains->Cloakroom Hook]].
    
    [if !hasCloak; append]
    It holds your [[cloak->Cloak]].
    
    [cont'd]
    The exit is a door to the [[east->Foyer]].
    
    
    :: Cloakroom Hook
    It's just a small brass hook, screwed to the wall.
    
    [if hasCloak]
    You could [[hang->hang cloak]] your [[cloak->Cloak]] here.
    
    [else]
    You could [[pick up your cloak and wear it]], if you like, or simply turn back to the [[cloak room->Cloakroom]].
    
    :: hang cloak
    hasCloak: false
    --
    {embed passage: 'Cloakroom'}
    
    :: pick up your cloak and wear it
    hasCloak: true
    --
    {embed passage: 'Cloakroom'}
    
    :: Bar
    room: 'Bar'
    --
    [if hasCloak]
    {embed passage: 'Darkness'}
    
    [else]
    The bar, much rougher than you'd have guessed after the opulence of the foyer to the north, is completely empty. There seems to be some sort of [[message->read message]] scrawled in the sawdust on the floor.
    
    
    :: read message
    The message, neatly marked in the sawdust, reads...
    
    [align center]
    _You have won_
    
    
    :: Darkness
    room: 'Darkness'
    --
    You can't see a thing! Not even the door you entered by--was it [[north->Foyer]], [[south->Darkness 2]], [[east->Darkness 2]] or [[west->Darkness 2]]?
    
    
    :: Darkness 2
    Blundering around in the dark isn't a good idea! You can't tell [[left->Darkness 3]] from [[right->Darkness 3]], let alone [[east->Darkness 3]] from [[west->Darkness 3]] or [[north->Foyer]] from [[south->Darkness 3]].
    
    
    :: Darkness 3
    No, this isn't getting you anywhere... Let's see, the door was [[south->Darkness 4]], wasn't it? So the exit must be [[north->Foyer]], unless you've gotten [[turned around->Darkness 4]].
    
    
    :: Darkness 4
    Oops, this is just a blank wall! But perhaps if you [[follow it around->Foyer]]...



.. |sphinxcontrib-twine-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |python-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-twine.svg
    :target: https://pypi.org/project/sphinxcontrib-twine


.. |docs-badge| image:: https://img.shields.io/readthedocs/sphinxcontrib-twine
    :target: https://sphinxcontrib-twine.readthedocs.io


.. |build-badge| image:: https://img.shields.io/github/actions/workflow/status/pypa/sphinxcontrib-twine/main.yml?branch=main
    :target: https://github.com/pypa/sphinxcontrib-twine/actions


.. |Twine| raw:: html

    <a href="https://twinery.org/" target="_blank">Twine</a>


.. |Chapbook| raw:: html

    <a href="https://klembot.github.io/chapbook/" target="_blank">Chapbook</a>
