=========================
Alabaster: a Sphinx theme
=========================

.. include:: ../README.rst

Features
========

* Easy ability to install/use as a Python package (tip o' the hat to `Dave &
  Eric's sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`_ for
  showing the way);
* Style tweaks compared to the source themes, such as better code-block
  alignment, Github button placement, page source link moved to footer,
  improved (optional) related-items sidebar item, and many more;
* Many customization hooks, including toggle of various sidebar & footer
  components; header/link/etc color control; etc;
* Improved documentation for all customizations (pre-existing & new).


Project background
==================

Alabaster is a modified (with permission) version of `Kenneth Reitz's
<http://kennethreitz.org>`_ `"krTheme" Sphinx theme 
<https://github.com/kennethreitz/kr-sphinx-themes>`_ (it's the one used 
in his `Requests <http://python-requests.org>`_ project). Kenneth's 
theme was itself originally based on Armin Ronacher's `Flask
<http://flask.pocoo.org/>`_ theme. Many thanks to both for their hard work.


Implementation notes
====================

* `Fabric #419 <https://github.com/fabric/fabric/issues/419>`_ contains a lot of
  general exposition & thoughts as I developed Alabaster, specifically with a
  mind towards using it on two nearly identical 'sister' sites (single-version
  www 'info' site & versioned API docs site).
* Alabaster includes/requires a tiny Sphinx extension on top of the theme
  itself; this is just so we can inject dynamic metadata (like Alabaster's own
  version number) into template contexts. It doesn't add any additional
  directives or the like, at least not yet.


.. toctree::
    :hidden:
    :glob:

    *
