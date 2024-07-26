=========
Changelog
=========

Next release (in development)
-----------------------------

:git_tag:`1.0.0` -- 2024-07-26
------------------------------

- Dropped support for Python 3.9 and earlier.
- Dropped support for Sphinx 6.1 and earlier.
- Use a new SVG image for the GitHub banner.
- :feature:`217` Use the new *searchfield* component for the search box.
  Patch by Tim Hoffmann.
- :feature:`104` Allow translating strings in ``relations.html``.
- :bug:`125` Do not underline linked images.
   Patch by Joshua Bronson.
- :bug:`169` Do not ignore the Pygments background colour.
  Patch by Matthias Geier.
- :bug:`174` Fix clipping caused by incorrect CSS breakpoints.

:git_tag:`0.7.16` -- 2024-01-10
-------------------------------

- :bug:`215` Do not display ``logo_name`` if it is set to ``False``.

:git_tag:`0.7.15` -- 2024-01-08
-------------------------------

- :feature:`213` Allow an arbitrary string in the ``logo_name`` option.
- :feature:`114` Improved sidebar CSS styles.
- :issue:`178` Deprecated ``canonical_url`` in favor of ``html_baseurl``.
- :bug:`200` Removed duplicate ``<meta name="viewport" ... />`` tag.
- :bug:`188` Removed underline from whitespace.
- :bug:`164` Removed ``type="text/javascript"`` from <script> elements.
- :bug:`161` Replaced ``&copy;`` with unicode decimal code entity ``#169;``.

:git_tag:`0.7.14` -- 2024-01-08
-------------------------------

- Dropped support for Python 3.8 and earlier.
- Dropped support for Sphinx 3.3 and earlier.
- :issue:`198` Fix horizontal scrolling on mobile.
- :issue:`206` Properly support the ``html_support_sphinx`` config value.
- :issue:`211` Fix the GitHub 'forkme' banner.
- Added ``alabaster_version_info`` to the HTML template context.
- Declare support for Python 3.13.
- Adopt the Ruff linter and formatter.
- Migrate from CircleCI to GitHub Actions.

:git_tag:`0.7.13` -- 2023-01-13
-------------------------------

- Modernized the project: s/Travis/Circle/ for CI,
  README badges, ``setup.cfg`` removal, metadata refresh, etc.
- Dropped support for Python 2 and Python <3.6. This
  includes various minor updates to work correctly with modern versions of
  Sphinx (1.6 at the very least). Thanks to Adam Turner for a pile of patches
  here.

  .. warning::
    This change is backwards incompatible if you're on an old Python version.

- Tweak CSS somewhat for compatibility with modern
  Sphinx versions' base stylesheet.

:git_tag:`0.7.12` -- 2018-10-02
-------------------------------

- On some browsers/platforms, 'badge'-style sidebar elements were
  displaying dotted underlines. This was unintentional and explicit styling has
  been added to remove them. Credit to Steven Loria.
- Reorganize the :doc:`customization page
  </customization>` to break up the now rather long list of "variables and
  feature toggles" into additional sections; includes alphabetizing those
  lists, to make it a bit easier to find docs for a specific setting.
- :feature:`132` (partially via :issue:`143`) Add a generic donation
  badge/url option (visually powered by https://shields.io/) as well as a
  service-specific donation option for `OpenCollective
  <https://opencollective.com>`_.

  We expect this to be followed-up on later with more service-specific options
  for services like Patreon. Thanks to Melanie Crutchfield for the report and
  Steven Loria for the initial patch.
- :bug:`128` Remove Gittip/Gratipay output from the ``donate.html`` sidebar
  component, since the actual service has been insolvent since 2017. The
  configuration options remain in place for the time being (to avoid breaking
  backwards compatibility) but no longer do anything. Thanks to Joe Alcorn for
  the report / original patchset.

  .. note::
    See the changelog entry for ``#132``, which re-introduces a more generic
    donation sidebar framework.

- :feature:`142` Add a ``tidelift_url`` option, which when set
  (default is ``None``/unset) adds a small text snippet to the
  ``donate.html`` sidebar component, linking to the given URL string. Thanks
  to Steven Loria for the patch.
- :bug:`141` Fix a typo in the code-block font family, which incorrectly
  specified ``Deja Vu Sans Mono`` instead of ``DejaVu Sans Mono``. This would
  primarily impact systems lacking the first two fonts (``Consolas`` and
  ``Menlo``) such as Linux desktops. Thanks to Ilya Trukhanov for catch &
  patch.

:git_tag:`0.7.11` -- 2018-06-18
-------------------------------

- :bug:`73` Clean up some problematic font issues:

  - Remove the outright broken Goudy Old Style, plus other mostly Adobe-only
    fonts, from the ``font_family`` config setting; it is now simply ``Georgia,
    serif`` which is what the majority of users were rendering anyways.
  - Clear out the default value of ``head_font_family`` (which contained
    ``Garamond``, a nice but also Adobe only font)
  - Set ``head_font_family`` so it falls back to the value of ``font_family``
    unless a user has explicitly set it themselves.

  .. note::
    You can always go back to the old values by :ref:`explicitly setting
    <theme-options>` ``font_family`` and/or ``head_font_family`` in your
    ``conf.py``'s ``html_theme_options``, e.g.:

    .. code-block:: python

        html_theme_options = {
            'description': 'My awesome project',
            'font_family': "goudy old style, minion pro, bell mt, Georgia, Hiragino Mincho Pro, serif",
        }

  .. warning::
    Depending on individual viewers' systems, this change *may* be **visually**
    backwards incompatible if you were not already overriding the font
    settings and those users had the fonts in question (which are not default
    on most systems).

    As seen in the note above, you can **always** override the new defaults to
    go back to the old behavior, using your config file.

- :feature:`18` (via :issue:`101`) Add optional *next* and
  *previous* links at the top and bottom of page content. Use theme option
  ``show_relbars`` to enable these. Credit: William Minchin.
- Miscellaneous project maintenance updates such as
  adding to Travis CI and enforcing the use of ``flake8``.
- :feature:`110` Add ``badge_branch`` option allowing
  configurability of which specific Git branch the Travis, Codecov, etc buttons
  default to. Credit: ``@TitanSnow``.
- :feature:`111` Add setuptools-level entrypoint for improved theme
  distribution compatibility. Thanks to Aaron Carlisle for the patch.

:git_tag:`0.7.10` -- 2017-02-28
-------------------------------

- :bug:`32` Update styling of various block-level elements such as admonitions
  (``.. note::``, ``.. warning::``, etc) and code blocks (``.. code::``) so
  they are no longer 'dedented' outside the main column of text they're
  embedded in. This is both a stylistic change and a bugfix, since e.g. nesting
  code blocks *within* note blocks looks actively broken. Thanks to Takayuki
  Shimizukawa for the report.
- :bug:`96` ``admonition_xref`` had a template typo preventing it from
  receiving styling; this has been fixed. Credit: Kenzie Togami.
- :bug:`95` Independently ran across
  `sphinx-doc/sphinx#3276 <https://github.com/sphinx-doc/sphinx/issues/3276>`_,
  namely that parameter lists become squashed together if one is running on
  Sphinx 1.4.x. While that fix was merged in Sphinx itself, we felt it prudent
  to include it in our own stylesheet as well, for immediate relief.

:git_tag:`0.7.9` -- 2016-07-25
------------------------------

- :feature:`6` (and :issue:`70`, both via :issue:`84`) Make all remaining
  hardcoded style colors configurable, plus related cleanup (such as improving
  differentiation of some admonition blocks such as ``warn`` and ``note``,
  ensuring generic admonitions are left untouched, etc). Credit:
  ``@ShadowKyogre``.
- :feature:`83` Expose Sphinx's toctree ``collapse`` option as the new
  ``sidebar_collapse`` config option. Credit: Eric Holscher.
- :feature:`80` Add support for ``<link rel="canonical">`` (i.e. canonical
  URLs). Thanks to Ben Gamari for the patch.
- :feature:`7` Generate real documentation site, both because the README is
  just too big now, and so we can `eat our own dog food
  <https://en.wikipedia.org/wiki/Eating_your_own_dog_food>`_.

:git_tag:`0.7.8` -- 2016-05-05
------------------------------

- #51 (via #67): Hide Github button if ``github_user`` and ``github_repo``
  aren't set. This is necessary since ``github_button`` defaults to True.
  Thanks to Sam Whited for the report & Dmitry Shachnev for the patch.
- #75: Use SVG version of the Travis-CI button. Thanks to Sebastian Wiesner for
  the patch.
- #41: Update the Github buttons to use a newer linked image & change the link
  to their docs. Thanks to Tomi Hukkalainen.
- #45 (via #46) Tweak styling of nested bullet lists to prevent an issue where
  they all collapse to the same indent level when viewed on smaller display
  sizes. Thanks to Bram Geron for catch & patch, and to Jochen Kupperschmidt
  for review/discussion.
- #44 (partial; via #57) Add an opt-in fixed sidebar behavior for users who
  prefer a sidebar that never scrolls out of view. Credit: Joe Cross.
- #61: Set a small-but-nonzero footnote width to work around a common browser
  display bug. Thanks to Konstantin Molchanov for catch & patch.
- #64: Add config options for font size and caption font size/family. Credit:
  Marçal Solà.
- #78: Add custom stylesheet support. (This release will thus be the last to
  merge simplistic style tweaks as feature toggles - only thorny CSS issues or
  actual template-related changes will be merged afterwards.)
- #65: Wrap the sidebar's "Navigation" header in Sphinx's translation helper so
  it gets translated if possible. Thanks to ``@uralbash``.
- #77: Fix image link styling to remove a bottom border which appears in some
  situations. Thanks to Eric Holscher for the patch & ``@barbara-sfx`` for the
  report.

:git_tag:`0.7.7` -- 2015-12-21
------------------------------

- Add some ``margin-bottom`` to ``table.field-list p`` so field lists (e.g.
  Python function parameter lists in docstrings) written as multiple
  paragraphs, look like actual paragraphs instead of all globbing together.
- Fix incorrect notes in README re: renamed ``github_button_*`` options - the
  ``button_`` was dropped but docs did not reflect this. Thanks to Nik Nyby.
- Fix ``sidebar_hr`` setting - stylesheet wasn't correctly referencing the
  right variable name. Thanks to Jannis Leidel.
- Allow configuring body text-align via ``body_text_align``. Credit to Marçal
  Solà.
- Fix a handful of mismatched/unclosed HTML tags in the templates. Thanks to
  Marvin Pinto for catch & patch.
- Add `Codecov <https://about.codecov.io>`_ badge support to sidebar.

:git_tag:`0.7.6` -- 2015-06-22
------------------------------

- Update how ``setup.py`` handles the ``README.rst`` file - load it explicitly
  as UTF-8 so the changelog containing non-ASCII characters doesn't generate
  ``UnicodeDecodeError`` in terminal environments whose default encoding is not
  UTF-8 or other Unicode-compatible encodings. Thanks to Arun Persaud for the
  report and Max Tepkeev for the suggested fix.
- Fix left-margin & padding styling for code blocks within list-item elements,
  making them consistent with earlier changes applied to top-level code blocks.
- Expose page & sidebar widths as theme options ``page_width`` and
  ``sidebar_width``. Their defaults are the same as the previously static
  values.

:git_tag:`0.7.5` -- 2015-06-15
------------------------------

- Honor Sphinx's core ``html_show_copyright`` option when rendering page
  footer. Thanks to Marcin Wojdyr for the report.
- Pre-history versions of Alabaster attempted to remove the "related"
  sub-navigation (typically found as next/previous links in other themes) but
  this didn't work right for mobile-oriented styling.

  This has been fixed by (re-)adding an improved sidebar nav element for these
  links and making its display controllable via the new ``show_related`` theme
  option (which defaults to ``false`` for backwards compatibility).

  .. note::
    To enable the related-links nav, you'll need to set ``show_related`` to
    ``true`` **and** add ``relations.html`` to your ``html_sidebars`` (we've
    updated the example config in this README to indicate this for new
    installs).

  Thanks to Tomi Pieviläinen for the bug report.
- Update the "Fork me on Github" banner image to use an ``https://`` URI so
  sites hosted over HTTPS don't encounter mixed-content errors. Thanks to
  ``@nikolas`` for the patch.
- Remove an orphaned ``</li>`` from the footer 'show source' section. Credit to
  Marcin Wojdyr.

:git_tag:`0.7.4` -- 2015-05-03
------------------------------

- Add ``code_highlight`` option (which includes general fixes to styling of
  code blocks containing highlighted lines). Thanks to Steven Loria.

:git_tag:`0.7.3` -- 2015-03-20
------------------------------

- Hide ``shadow`` related styles on bibliography elements, in addition to the
  earlier change re: ``border``. Thanks again to Philippe Dessus.

:git_tag:`0.7.2` -- 2015-03-10
------------------------------

- Updated CSS stylesheets to apply monospace styling to both ``tt`` and
  ``code`` elements, instead of just to ``tt``. This addresses a change in HTML
  generation in Sphinx 1.3 while retaining support for Sphinx 1.2. Thanks to
  Eric Holscher for the heads up.

:git_tag:`0.7.1` -- 2015-02-27
------------------------------

- Finally add a changelog. To the README, for now, because a full doc site
  isn't worthwhile just yet.
- Allow configuring a custom Github banner image (instead of simply toggling a
  default on or off). Thanks to Nicola Iarocci for the original patch.
- Explicitly note Python version support in the README and ``setup.py``.
- Update Github button image link to use the newly-available HTTPS version of
  the URL; this helps prevent errors on doc pages served via HTTPS. Thanks to
  Gustavo Narea for the report.
- Add control over the font size & family of code blocks. Credit to Steven
  Loria.
- Allow control over font family of body text and headings. Thanks to Georg
  Brandl.
- Stylize ``.. seealso::`` blocks same as ``.. note::`` blocks for
  consistency's sake (previously, ``.. seealso::`` used the Sphinx default
  styling, which clashed). We may update these again later but for now, this is
  an improvement! Thanks again to Steven Loria.
- Allow control over CSS ``font-style`` for the site description/tagline
  element. Credit: Steven Loria.
- Add styling to disable default cell borders on ``.. bibliography::``
  directives' output. Thanks to Philippe Dessus for the report.

:git_tag:`0.6.2` -- 2014-11-25
------------------------------

- Make ``.. warn::`` blocks have a pink background (instead of having no
  background, which was apparently an oversight of the themes Alabaster is
  based on) and also make that color configurable.

:git_tag:`0.6.1` -- 2014-09-04
------------------------------

- Update Gittip support to acknowledge the service's rename to Gratipay.

:git_tag:`0.6.0` -- 2014-04-17
------------------------------

- Allow hiding the 'powered by' section of the footer.
- Fix outdated name in ``setup.py`` URL field.

:git_tag:`0.5.1` -- 2014-04-15
------------------------------

- Fix a bug in the new Travis support, re: its default value.

:git_tag:`0.5.0` -- 2014-04-09
------------------------------

- Add support for sidebar Travis status buttons.

:git_tag:`0.4.1` -- 2014-04-06
------------------------------

- Fix an inaccuracy in the description of ``logo_text_align``.
- Update logo & text styling to be more sensible.

:git_tag:`0.4.0` -- 2014-04-06
------------------------------

- Add an option to allow un-hiding one's toctree.

:git_tag:`0.3.1` -- 2014-03-13
------------------------------

- Improved Python 3 compatibility.
- Update styling of changelog pages generated by `bitprophet/releases
  <https://github.com/bitprophet/releases>`_.

:git_tag:`0.3.0` -- 2014-02-03
------------------------------

- Display Alabaster version in footers alongside Sphinx version (necessitating
  use of a mini Sphinx extension) plus other footer tweaks.

:git_tag:`0.2.0` -- 2014-01-28
------------------------------

- Allow control of logo replacement text's alignment.
- Add customized navigation sidebar element.
- Tweak page margins a bit.
- Add a 3rd level of medium-gray to the stylesheet & apply in a few places.

:git_tag:`0.1.0` -- 2013-12-31
------------------------------

- First tagged/PyPI'd version.
