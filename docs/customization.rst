=============
Customization
=============

Alabaster's behavior & style can be customized in multiple ways:

* Various template-level or nontrivial-style settings can be configured via
  your ``conf.py`` in ``html_theme_options``; see :ref:`theme-options`.
* As of Alabaster 0.7.8, you can provide your own CSS stylesheet overrides via
  a :ref:`custom stylesheet <custom-stylesheet>`. This is suitable for changes
  that only need minor CSS modifications.

  .. note::
    Some theme options implemented prior to 0.7.8 would have been more suitable
    as local custom stylesheet overrides. Therefore:
    
    * We no longer accept feature requests which are more appropriately solved
      by using this functionality instead.
    * In future backwards-incompatible versions we may deprecate some of those
      options; as such we highly recommend leveraging the custom stylesheet
      whenever possible, even if an option is present below.
      
        * When in doubt, simply check `the built-in stylesheet's template
          <https://github.com/bitprophet/alabaster/blob/master/alabaster/static/alabaster.css_t>`_
          to see whether the option you're looking at is a basic variable
          insertion or something more complicated.)


.. _custom-stylesheet:

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


.. _theme-options:

Theme options
=============

Alabaster's primary configuration route is the ``html_theme_options`` variable,
set in ``conf.py`` alongside the rest, e.g.:

.. code-block:: python

    html_theme_options = {
        'logo': 'logo.png',
        'github_user': 'bitprophet',
        'github_repo': 'alabaster',
    }

The following subsections detail available such options, including notes about
behavior & default values.

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
* ``github_user``, ``github_repo``: Used by ``github_button`` and
  ``github_banner`` (see below); does nothing if both of those are set to
  ``false``.
* ``github_button``: ``true`` or ``false`` (default: ``true``) - whether to
  link to your Github.

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

* ``badge_branch``: Set which branch is used in Travis, CodeCov, etc badges.
  Defaults to ``master``.

* ``travis_button``: ``true``, ``false`` or a Github-style ``"account/repo"``
  string - used to display a `Travis-CI <https://travis-ci.org>`_ build status
  button in the sidebar. If ``true``, uses your ``github_(user|repo)``
  settings; defaults to ``false.``
* ``codecov_button``: ``true``, ``false`` or a Github-style ``"account/repo"``
  string - used to display a `Codecov <https://codecov.io>`_ build status
  button in the sidebar. If ``true``, uses your ``github_(user|repo)``
  settings; defaults to ``false.``
* ``analytics_id``: Set to your `Google Analytics
  <http://www.google.com/analytics/>`_ ID (e.g. ``UA-#######-##``) to enable
  tracking.
* ``touch_icon``: Path to an image (as with ``logo``, relative to
  ``$PROJECT/_static/``) to be used for an iOS application icon, for when
  pages are saved to an iOS device's home screen via Safari.
* ``canonical_url``: If set, is used as the base URL (set before the relative
  path/pagename) for a ``<link rel="canonical">`` `canonical URL
  <https://support.google.com/webmasters/answer/139066?rd=1>`_ header tag.

  .. note:: This value must end with a trailing slash.

* ``extra_nav_links``: Dictionary mapping link names to link targets; these
  will be added in a UL below the main sidebar navigation (provided you've
  enabled ``navigation.html`` via the ``html_sidebars`` option; see
  :doc:`installation`.) Useful for static links outside your Sphinx doctree.
* ``sidebar_includehidden``: Boolean determining whether the TOC sidebar
  should include hidden Sphinx toctree elements. Defaults to ``true`` so you
  can use ``:hidden:`` in your index page's root toctree & avoid having 2x
  copies of your navigation on your landing page.
* ``sidebar_collapse``: Boolean determining whether  all TOC entries that 
   are not ancestors of the current page are collapsed.
   You can read more about this in the Sphinx toctree 
   `docs <http://www.sphinx-doc.org/en/stable/templating.html#toctree>`_.
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
* ``show_relbars``: ``true`` or ``false``, defaults to ``false`` - used to
  display *next* and *previous* links above and below the main page content. If
  you only want to display one, this setting can be further overridden through
  the ``show_relbar_top`` and ``show_relbar_bottom`` settings.

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
* ``relbar_border``: Color of border between bar holding *next* and *previous*
  links, and the rest of the page content. Defaults to ``gray_2``.

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
