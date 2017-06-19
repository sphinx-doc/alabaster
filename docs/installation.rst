============
Installation
============

The bare minimum required to install Alabaster is as follows:

* If you're on **Sphinx 1.2 or older**:

    * ``pip install alabaster`` or equivalent.
    * Add the following to your ``conf.py`` so Alabaster's theme location &
      mini-extension are located & loaded:

       .. code-block:: python

            import alabaster

            html_theme_path = [alabaster.get_path()]
            extensions = ['alabaster']
            html_theme = 'alabaster'

    * If you've installed Alabaster by hand (without using ``pip``) and/or are
      doing funky things to your PYTHONPATH, you may need to replace the
      ``alabaster.get_path()`` call with your own explicit string, as per `the
      Sphinx config docs
      <http://sphinx-doc.org/config.html#confval-html_theme_path>`_.

* If you have **Sphinx 1.3 or above**:

    * You already have Alabaster installed as a dependency! No need to manually
      install it or explicitly load it.

      .. note::
        If you distribute your documentation via the excellent `Read the Docs
        <https://readthedocs.org>`_, you may need to explicitly enable
        Alabaster (as RTD defaults to using its own theme) by adding this line
        to your ``conf.py``::

            html_theme = 'alabaster'

* **Either way**, add an explicit ``html_sidebars`` setting so Alabaster's
  customized sidebar templates are loaded:
   
   .. code-block:: python
    
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
