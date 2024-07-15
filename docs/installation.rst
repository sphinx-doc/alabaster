============
Installation
============

Alabaster requires **Sphinx 6.2 or newer**, and is included as the default
theme.

.. note::
  If you distribute your documentation via `Read the Docs
  <https://readthedocs.org>`_, you will need to explicitly enable
  Alabaster by adding this line to your ``conf.py``:

  .. code-block:: python

     html_theme = 'alabaster'

To set-up Alabaster, add an explicit ``html_sidebars`` setting so
Alabaster's customized sidebar templates are loaded:
   
   .. code-block:: python
    
        html_sidebars = {
            '**': [
                'about.html',
                'searchfield.html',
                'navigation.html',
                'relations.html',
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
  <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars>`_ for details on
  how this setting behaves.
* Alabaster provides ``about.html`` (logo, github button + blurb),
  ``donate.html`` (donation/support buttons/links) and ``navigation.html`` (a
  more flexible version of the builtin ``localtoc``/``globaltoc`` templates).
  ``searchfield.html`` comes with Sphinx itself.


.. _static-path:

Static path for images and/or custom stylesheet
-----------------------------------------------

If you're using any of the image-related options listed on :doc:`customization`
(``logo`` or ``touch-icon``) or a :ref:`custom stylesheet <custom-stylesheet>`,
you'll also want to tell Sphinx where to get these files from. If so, add a
line like this (changing the path if necessary; see `the Sphinx docs for
'html_static_path'
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path>`_) to your ``conf.py``:

.. code-block:: python

    html_static_path = ['_static']
