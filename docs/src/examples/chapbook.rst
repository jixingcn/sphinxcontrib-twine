Chapbook
########

A story format of twine - |Chapbook|.


Test
****

.. twine::
    :format: Chapbook
    :title: Test
    :width: 100%
    :height: 500

    :: StoryTitle
    Test in Chapbook

    :: Start
    Start


Conditional Statements
**********************

Source from `Conditional Statements <https://twinery.org/cookbook/conditionalstatements/chapbook/chapbook_conditionalstatements.html>`_.

.. twine::
    :format: Chapbook
    :width: 100%
    :height: 500

    :: StoryTitle
    Conditional Statements in Chapbook
    
    :: Start
    animal: "horse"
    --
    [if animal === "dog"]
    It's a dog!
    [else]
    It's a horse!
    [continue]


CSS Selectors
*************

Source from `CSS Selectors <https://twinery.org/cookbook/cssselectors/chapbook/chapbook_cssselectors.html>`_.

.. twine::
    :format: Chapbook
    :width: 100%
    :height: 500

    :: StoryTitle
    CSS Selectors in Chapbook
    
    :: UserStylesheet[stylesheet]
    #backdrop {
        border: 5px solid green;
    }
    
    #page {
        border: 2px solid red;
    }
    
    #page article>:first-child {
        border: 1px solid blue;
    }
    
    :: Start
    The backdrop has a green border; it contains this page (red border) and the article (blue border).
    
    [[Second]]
    
    :: Second
    This passage also has a blue border.


External JavaScript
*******************

Source from `External JavaScript <https://twinery.org/cookbook/importexternaljs/chapbook/chapbook_importexternaljs.html>`_.

.. twine::
    :format: Chapbook
    :width: 100%
    :height: 500

    :: StoryTitle
    Chapbook: Importing External JS
    
    :: UserScript[script]
    // The following code is used from MDN for
    // dynamically importing scripts
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement#Dynamically_importing_scripts
    
    window.setup = {};
    
    setup.loadError = function(oError) {
      throw new URIError("The script " + oError.target.src + " didn't load correctly.");
    };
    
    setup.loadScript = function(url, onloadFunction) {
      var newScript = document.createElement("script");
      newScript.onerror = setup.loadError;
      if (onloadFunction) { newScript.onload = onloadFunction; }
      document.head.appendChild(newScript);
      newScript.async = true;
      newScript.src = url;
    };
    
    
    :: Start
    <div id="drawArea"></div>
    [JavaScript]
    setup.loadScript("https://ajax.googleapis.com/ajax/libs/threejs/r84/three.min.js", function() {
      var scene = new THREE.Scene();
      var camera = new THREE.PerspectiveCamera(
        75,
        1,
        0.1,
        1000 );
    
      var renderer = new THREE.WebGLRenderer();
      renderer.setSize( 250, 250 );
      document.getElementById("drawArea").appendChild( renderer.domElement );
    
      var geometry = new THREE.BoxGeometry( 1, 1, 1 );
      var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
      var cube = new THREE.Mesh( geometry, material );
      scene.add( cube );
    
      camera.position.z = 5;
    
      var animate = function () {
        requestAnimationFrame( animate );
    
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
    
        renderer.render( scene, camera );
      };
    
      animate();
    
    });
    
    [continued]


.. |Chapbook| raw:: html

    <a href="https://klembot.github.io/chapbook/" target="_blank">Chapbook</a>
