============
Installation
============

The bare minimum required to install Alabaster is as follows:

#. If you have Sphinx 1.3 or above, you already have Alabaster installed as a
   dependency; and since it is the default theme, you may skip everything but
   ``html_sidebars`` in the below ``conf.py`` snippet.

    * Users on Sphinx 1.2 or older may simply ``pip install alabaster`` (or
      equivalent).

#. Enable the 'alabaster' theme, mini-extension, and sidebar templates in your
   ``conf.py``:
   
   .. code-block:: python
    
        import alabaster
        
        html_theme_path = [alabaster.get_path()]
        extensions = ['alabaster']
        html_theme = 'alabaster'
        html_sidebars = {
            '**': [
                'about.html',
                'navigation.html',
                'relations.html',
                'searchbox.html',
                'donate.html',
            ]
        }

That's it! You now have the standard Alabaster theme set up. Read on for more
core configuration concerns, or see :doc:`customization` for feature/style
options.

Theme location
--------------

The function ``alabaster.get_path`` dynamically returns Alabaster's install
location, ensuring that Sphinx can find and load it regardless of where/how
you installed Alabaster. Using it is highly recommended.

If you've manually installed Alabaster and/or are doing funky things to your
PYTHONPATH, you may need to replace the ``alabaster.get_path()`` call with your
own explicit string, as per `the Sphinx config docs
<http://sphinx-doc.org/config.html#confval-html_theme_path>`_.


Sidebars
--------

Feel free to adjust ``html_sidebars`` as desired - the theme is designed
assuming you'll always have ``about.html`` activated, but otherwise it doesn't
care much.

* See `the Sphinx docs
  <http://sphinx-doc.org/config.html#confval-html_sidebars>`_ for details on
  how this setting behaves.
* Alabaster provides ``about.html`` (logo, github button + blurb),
  ``donate.html`` (Gratipay blurb/button) and ``navigation.html`` (a more
  flexible version of the builtin ``localtoc``/``globaltoc`` templates).
  ``searchbox.html`` comes with Sphinx itself.


.. _static-path:

Static path for images and/or custom stylesheet
-----------------------------------------------

If you're using any of the image-related options listed on :doc:`customization`
(``logo`` or ``touch-icon``) or a :ref:`custom stylesheet <custom-stylesheet>`,
you'll also want to tell Sphinx where to get these files from. If so, add a
line like this (changing the path if necessary; see `the Sphinx docs for
'html_static_path'
<http://sphinx-doc.org/config.html?highlight=static#confval-html_static_path>`_) to your ``conf.py``:

.. code-block:: python

    html_static_path = ['_static']
