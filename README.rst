=========================
Alabaster: a Sphinx theme
=========================

What is Alabaster?
==================

Alabaster is a visually (c)lean, responsive, configurable theme for the
`Sphinx`_ documentation system. It is Python 2+3 compatible.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is selected
as the default theme.

Live examples of this theme can be seen on `paramiko.org
<http://paramiko.org>`_, `fabfile.org <http://fabfile.org>`_ and `pyinvoke.org
<http://pyinvoke.org>`_.

A changelog_ can be found at the bottom of this page.


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


Installation
============

The bare minimum required to install is as follows:

#. ``pip install alabaster`` (or equivalent).
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
configuration options/concerns.

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

Images
------

If you're using either of the image-related options outlined below (``logo`` or
``touch-icon``), you'll also want to tell Sphinx where to get your images from.
If so, add a line like this (changing the path if necessary; see `the Sphinx
docs for 'html_static_path'
<http://sphinx-doc.org/config.html?highlight=static#confval-html_static_path>`_):

.. code-block:: python

    html_static_path = ['_static']


Custom stylesheet
=================

If you need to modify Alabaster's default CSS styles in a way not covered by
the theme options from the next section, you may provide a custom CSS
stylesheet as follows:

* Create a file named ``custom.css`` anywhere you prefer (typically
  ``_static/``, but this is solely convention) containing your desired
  overrides to the CSS found in Alabaster's ``static/alabaster_css_t``.
* Set the core Sphinx option `html_static_path
  <http://www.sphinx-doc.org/en/stable/config.html#confval-html_static_path>`_
  to either that file's path, or the directory it lives within.

.. note::
    As of Alabaster 0.7.8, we will stop accepting feature requests which are
    more appropriately solved by using this functionality instead.


Theme options
=============

Alabaster's primary configuration route is the ``html_theme_options`` variable,
set in ``conf.py`` alongside the rest. A brief example (*note*: snippet doesn't
include all possible options, see following list!):

.. code-block:: python

    html_theme_options = {
        'logo': 'logo.png',
        'github_user': 'bitprophet',
        'github_repo': 'alabaster',
    }

Variables and feature toggles
-----------------------------

* ``logo``: Relative path (from ``$PROJECT/_static/``) to a logo image, which
  will appear in the upper left corner above the name of the project.

  * If ``logo`` is not set, your ``project`` name setting (from the top
    level Sphinx config) will be used in a text header instead. This
    preserves a link back to your homepage from inner doc pages.

* ``logo_name``: Set to ``true`` to insert your site's ``project`` name
  under the logo image as text. Useful if your logo doesn't include the
  project name itself. Defaults to ``false``.
* ``logo_text_align``: Which CSS ``text-align`` value to use for logo text
  (if there is any.)
* ``body_text_align``: Which CSS ``text-align`` value to use for body text
  (if there is any.)
* ``description``: Text blurb about your project, to appear under the logo.
* ``description_font_style``: Which CSS ``font-style`` to use for description
  text. Defaults to ``normal``.
* ``github_user``, ``github_repo``: Used by ``github_button`` and ``github_banner``
  (see below); does nothing if both of those are set to ``false``.
* ``github_button``: ``true`` or ``false`` (default: ``true``) - whether to link to
  your Github.

   * If ``true``, requires that you set ``github_user`` and ``github_repo``.
   * See also these other related options, which behave as described in
     `Github Buttons' documentation
     <https://ghbtns.com>`_:

      * ``github_type``: Defaults to ``watch``.
      * ``github_count``: Defaults to ``true``.

* ``github_banner``: ``true`` or ``false`` (default: ``false``) - whether to
  apply a 'Fork me on Github' banner in the top right corner of the page.

   * If ``true``, requires that you set ``github_user`` and ``github_repo``.
   * May also submit a string file path (as with ``logo``, relative to
     ``$PROJECT/_static/``) to be used as the banner image instead of the
     default.

* ``travis_button``: ``true``, ``false`` or a Github-style ``"account/repo"``
  string - used to display a `Travis-CI <https://travis-ci.org>`_ build status
  button in the sidebar. If ``true``, uses your ``github_(user|repo)``
  settings; defaults to ``false.``
* ``codecov_button``: ``true``, ``false`` or a Github-style
  ``"account/repo"`` string - used to display a `Codecov`_
  build status button in the sidebar. If ``true``, uses your
  ``github_(user|repo)`` settings; defaults to ``false.``
* ``gratipay_user``: Set to your `Gratipay <https://gratipay.com>`_ username
  if you want a Gratipay 'Donate' section in your sidebar.

  * This used to be ``gittip_user`` before that service changed its name to
    Gratipay; we've left the old setting in place as an alias for backwards
    compatibility reasons. It may be removed in the future.
  * If both options are given, ``gratipay_user`` wins.

* ``analytics_id``: Set to your `Google Analytics
  <http://www.google.com/analytics/>`_ ID (e.g. ``UA-#######-##``) to enable
  tracking.
* ``touch_icon``: Path to an image (as with ``logo``, relative to
  ``$PROJECT/_static/``) to be used for an iOS application icon, for when
  pages are saved to an iOS device's home screen via Safari.
* ``extra_nav_links``: Dictionary mapping link names to link targets; these
  will be added in a UL below the main sidebar navigation (provided you've
  enabled ``navigation.html``.) Useful for static links outside your Sphinx
  doctree.
* ``sidebar_includehidden``: Boolean determining whether the TOC sidebar
  should include hidden Sphinx toctree elements. Defaults to ``true`` so you
  can use ``:hidden:`` in your index page's root toctree & avoid having 2x
  copies of your navigation on your landing page.
* ``show_powered_by``: Boolean controlling display of the ``Powered by
  Sphinx N.N.N. & Alabaster M.M.M`` section of the footer. When ``true``, is
  displayed next to the copyright information; when ``false``, is hidden.
* ``show_related``: Boolean controlling whether the 'next/previous/related'
  secondary navigation elements are hidden or displayed. Defaults to ``false``
  since on many sites these elements are superfluous.
* ``page_width``: CSS width specifier controlling default content/page width.
  Defaults to ``940px``.
* ``sidebar_width``: CSS width specifier controlling default sidebar width.
  Defaults to ``220px``.
* ``fixed_sidebar``: Makes the sidebar 'fixed' or pinned in place, so that the
  main body of the page scrolls but the sidebar remains visible. (Applies only
  to desktop window sizes; the mobile view is unaffected.) Defaults to
  ``false``.

Style colors
------------

These should be fully qualified CSS color specifiers such as ``#004B6B`` or
``#444``. The first few items in the list are "global" colors used as defaults
for many of the others; update these to make sweeping changes to the
colorscheme. The more granular settings can be used to override as needed.

* ``gray_1``: Dark gray.
* ``gray_2``: Light gray.
* ``gray_3``: Medium gray.
* ``pink_1``: Light pink.
* ``pink_2``: Medium pink.
* ``body_text``: Main content text.
* ``footer_text``: Footer text (includes links.)
* ``link``: Non-hovered body links.
* ``link_hover``: Body links, hovered.
* ``sidebar_header``: Sidebar headers. Defaults to ``gray_1``.
* ``sidebar_text``: Sidebar paragraph text.
* ``sidebar_link``: Sidebar links (there is no hover variant.) Applies to
  both header & text links. Defaults to ``gray_1``.
* ``sidebar_link_underscore``: Sidebar links' underline (technically a
  bottom-border).
* ``sidebar_search_button``: Background color of the search field's 'Go'
  button.
* ``sidebar_list``: Foreground color of sidebar list bullets & unlinked text.
* ``sidebar_hr``: Color of sidebar horizontal rule dividers. Defaults to
  ``gray_3``.
* ``anchor``: Foreground color of section anchor links (the 'paragraph'
  symbol that shows up when you mouseover page section headers.)
* ``anchor_hover_fg``: Foreground color of section anchor links (as above)
  when moused over. Defaults to ``gray_1``.
* ``anchor_hover_bg``: Background color of above.
* ``note_bg``: Background of ``.. note::`` blocks. Defaults to ``gray_2``.
* ``note_border``: Border of same.
* ``seealso_bg``: Background of ``.. seealso::`` blocks. Defaults to
  ``gray_2``.
* ``seealso_border``: Border of same.
* ``warn_bg``: Background of ``.. warn::`` blocks. Defaults to ``pink_1``.
* ``warn_border``: Border of same. Defaults to ``pink_2``.
* ``footnote_bg``: Background of footnote blocks.
* ``footnote_border``: Border of same. Defaults to ``gray_2``.
* ``pre_bg``: Background of preformatted text blocks (including code
  snippets.) Defaults to ``gray_2``.
* ``narrow_sidebar_bg``: Background of 'sidebar' when narrow window forces
  it to the bottom of the page.
* ``narrow_sidebar_fg``: Text color of same.
* ``narrow_sidebar_link``: Link color of same. Defaults to ``gray_3``.
* ``code_highlight``: Color of highlight when using ``:emphasize-lines:`` in a code block.

Fonts
-----

* ``font_family``: Font family of body text.  Defaults to ``'goudy old style',
  'minion pro', 'bell mt', Georgia, 'Hiragino Mincho Pro', serif``.
* ``font_size``: Font size of body text. Defaults to ``17px`` (``1.0625em``).
* ``head_font_family``: Font family of headings.  Defaults to ``'Garamond',
  'Georgia', serif``.
* ``code_font_size``: Font size of code block text. Defaults to ``0.9em``.
* ``code_font_family``: Font family of code block text. Defaults to
  ``'Consolas', 'Menlo', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono',
  monospace``.
* ``caption_font_size``: Font size of caption block text. Defaults to ``font-size``.
* ``caption_font_family``: Font family of caption block text. Defaults to ``font-family``.

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


.. _changelog:

Changelog
=========

0.1.0 (2013-12-31)
------------------

* First tagged/PyPI'd version.

0.2.0 (2014-01-28)
------------------

* Allow control of logo replacement text's alignment.
* Add customized navigation sidebar element.
* Tweak page margins a bit.
* Add a 3rd level of medium-gray to the stylesheet & apply in a few places.

0.3.0 (2014-02-03)
------------------

* Display Alabaster version in footers alongside Sphinx version. (This
  necessitates using a mini Sphinx extension).
* Other footer tweaks.

0.3.1 (2014-03-13)
------------------

* Improved Python 3 compatibility.
* Update styling of changelog pages generated by `bitprophet/releases
  <https://github.com/bitprophet/releases>`_.

0.4.0 (2014-04-06)
------------------

* Add an option to allow un-hiding one's toctree.

0.4.1 (2014-04-06)
------------------

* Fix an inaccuracy in the descriptin of ``logo_text_align``.
* Update logo & text styling to be more sensible.

0.5.0 (2014-04-09)
------------------

* Add support for sidebar Travis status buttons.

0.5.1 (2014-04-15)
------------------

* Fix a bug in the new Travis support, re: its default value.

0.6.0 (2014-04-17)
------------------

* Allow hiding the 'powered by' section of the footer.
* Fix outdated name in ``setup.py`` URL field.

0.6.1 (2014-09-04)
------------------

* Update Gittip support to acknowledge the service's rename to Gratipay.

0.6.2 (2014-11-25)
------------------

* Make ``.. warn::`` blocks have a pink background (instead of having no
  background, which was apparently an oversight of the themes Alabaster is
  based on) and also make that color configurable.

0.7.1 (2015-02-27)
------------------

.. note::
    There is no 0.7.0, there was some PyPI fun and replacing sdists isn't
    permitted :)

* Finally add a changelog. To the README, for now, because a full doc site
  isn't worthwhile just yet.
* Allow configuring a custom Github banner image (instead of simply toggling a
  default on or off). Thanks to Nicola Iarocci for the original patch.
* Explicitly note Python version support in the README and ``setup.py``.
* Update Github button image link to use the newly-available HTTPS version of
  the URL; this helps prevent errors on doc pages served via HTTPS. Thanks to
  Gustavo Narea for the report.
* Add control over the font size & family of code blocks. Credit to Steven
  Loria.
* Allow control over font family of body text and headings. Thanks to Georg
  Brandl.
* Stylize ``.. seealso::`` blocks same as ``.. note::`` blocks for
  consistency's sake (previously, ``.. seealso::`` used the Sphinx default
  styling, which clashed). We may update these again later but for now, this is
  an improvement! Thanks again to Steven Loria.
* Allow control over CSS ``font-style`` for the site description/tagline
  element. Credit: Steven Loria.
* Add styling to disable default cell borders on ``.. bibliography::``
  directives' output. Thanks to Philippe Dessus for the report.

0.7.2 (2015-03-10)
------------------

* Updated CSS stylesheets to apply monospace styling to both ``tt`` and
  ``code`` elements, instead of just to ``tt``. This addresses a change in HTML
  generation in Sphinx 1.3 while retaining support for Sphinx 1.2. Thanks to
  Eric Holscher for the heads up.

0.7.3 (2015-03-20)
------------------

* Hide ``shadow`` related styles on bibliography elements, in addition to the
  earlier change re: ``border``. Thanks again to Philippe Dessus.

0.7.4 (2015-05-03)
------------------

* Add ``code_highlight`` option (which includes general fixes to styling of
  code blocks containing highlighted lines). Thanks to Steven Loria.

0.7.5 (2015-06-15)
------------------

* Honor Sphinx's core ``html_show_copyright`` option when rendering page
  footer. Thanks to Marcin Wojdyr for the report.
* Pre-history versions of Alabaster attempted to remove the "related"
  sub-navigation (typically found as next/previous links in other themes) but
  this didn't work right for mobile-oriented styling.

  This has been fixed by (re-)adding an improved sidebar nav element for these
  links and making its display controllable via the new ``show_related`` theme
  option (which defaults to ``false`` for backwards compatibility).

  **NOTE**: to enable the related-links nav, you'll need to set
  ``show_related`` to ``true`` **and** add ``relations.html`` to your
  ``html_sidebars`` (we've updated the example config in this README to
  indicate this for new installs).

  Thanks to Tomi Pieviläinen for the bug report.
* Update the "Fork me on Github" banner image to use an ``https://`` URI so
  sites hosted over HTTPS don't encounter mixed-content errors. Thanks to
  ``@nikolas`` for the patch.
* Remove an orphaned ``</li>`` from the footer 'show source' section. Credit to
  Marcin Wojdyr.

0.7.6 (2015-06-22)
------------------

* Update how ``setup.py`` handles the ``README.rst`` file - load it explicitly
  as UTF-8 so the changelog containing non-ASCII characters doesn't generate
  ``UnicodeDecodeError`` in terminal environments whose default encoding is not
  UTF-8 or other Unicode-compatible encodings. Thanks to Arun Persaud for the
  report and Max Tepkeev for the suggested fix.
* Fix left-margin & padding styling for code blocks within list-item elements,
  making them consistent with earlier changes applied to top-level code blocks.
* Expose page & sidebar widths as theme options ``page_width`` and
  ``sidebar_width``. Their defaults are the same as the previously static
  values.

0.7.7 (2015-12-21)
------------------

* Add some ``margin-bottom`` to ``table.field-list p`` so field lists (e.g.
  Python function parameter lists in docstrings) written as multiple
  paragraphs, look like actual paragraphs instead of all globbing together.
* Fix incorrect notes in README re: renamed ``github_button_*`` options - the
  ``button_`` was dropped but docs did not reflect this. Thanks to Nik Nyby.
* Fix ``sidebar_hr`` setting - stylesheet wasn't correctly referencing the
  right variable name. Thanks to Jannis Leidel.
* Allow configuring body text-align via ``body_text_align``. Credit to Marçal
  Solà.
* Fix a handful of mismatched/unclosed HTML tags in the templates. Thanks to
  Marvin Pinto for catch & patch.
* Add `Codecov`_ badge support to sidebar.

0.7.8 (2016-05-05)
------------------

* #51 (via #67): Hide Github button if ``github_user`` and ``github_repo``
  aren't set. This is necessary since ``github_button`` defaults to True.
  Thanks to Sam Whited for the report & Dmitry Shachnev for the patch.
* #75: Use SVG version of the Travis-CI button. Thanks to Sebastian Wiesner for
  the patch.
* #41: Update the Github buttons to use a newer linked image & change the link
  to their docs. Thanks to Tomi Hukkalainen.
* #45 (via #46) Tweak styling of nested bullet lists to prevent an issue where
  they all collapse to the same indent level when viewed on smaller display
  sizes. Thanks to Bram Geron for catch & patch, and to Jochen Kupperschmidt
  for review/discussion.
* #44 (partial; via #57) Add an opt-in fixed sidebar behavior for users who
  prefer a sidebar that never scrolls out of view. Credit: Joe Cross.
* #61: Set a small-but-nonzero footnote width to work around a common browser
  display bug. Thanks to Konstantin Molchanov for catch & patch.
* #64: Add config options for font size and caption font size/family. Credit:
  Marçal Solà.
* #78: Add custom stylesheet support. (This release will thus be the last to
  merge simplistic style tweaks as feature toggles - only thorny CSS issues or
  actual template-related changes will be merged afterwards.)
* #65: Wrap the sidebar's "Navigation" header in Sphinx's translation helper so
  it gets translated if possible. Thanks to ``@uralbash``.
* #77: Fix image link styling to remove a bottom border which appears in some
  situations. Thanks to Eric Holscher for the patch & ``@barbara-sfx`` for the
  report.


.. _Codecov: https://codecov.io
.. _Sphinx: http://sphinx-doc.org
