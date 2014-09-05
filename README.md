# Alabaster: a Sphinx theme

This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his [Requests](https://python-requests.org) project), which was itself
originally based on @mitsuhiko's theme used for
[Flask](http://flask.pocoo.org/) & related projects.

A live example of what this theme looks like can be seen on e.g.
[paramiko.org](http://paramiko.org).

Features (compared to Kenneth's original theme):

* Easy ability to install/use as a Python package (tip o' the hat to [Dave &
  Eric's sphinx_rtd_theme](https://github.com/snide/sphinx_rtd_theme) for
  showing the way);
* Style tweaks, such as better code-block alignment, Gratipay and Github button
  placement, page source link moved to footer, etc;
* Additional customization hooks, such as header/link/etc colors;
* Improved documentation for all customizations (pre-existing & new).

To use:

1. `pip install alabaster` (or equivalent command)
1. Enable the 'alabaster' theme + mini-extension in your `conf.py`:

   ```python
   import alabaster

   html_theme_path = [alabaster.get_path()]
   extensions = ['alabaster']
   html_theme = 'alabaster'
   html_sidebars = {
       '**': [
           'about.html', 'navigation.html', 'searchbox.html', 'donate.html',
       ]
   }
   ```

    * Modify the call to `abspath` if your `_themes` folder doesn't live right
    next to your `conf.py`.
    * Feel free to adjust `html_sidebars` as desired - the theme is designed
    assuming you'll have `about.html` activated, but otherwise it doesn't care
    much.
        * See [the Sphinx
        docs](http://sphinx-doc.org/config.html#confval-html_sidebars) for
        details on how this setting behaves.
        * Alabaster provides `about.html` (logo, github buttom + blurb),
        `donate.html` (Gratipay blurb/button) and `navigation.html` (a more
        flexible version of the builtin `localtoc`/`globaltoc` templates); the
        others listed come from Sphinx itself.

1. If you're using either of the image-related options outlined below (logo or
   touch-icon), you'll also want to tell Sphinx where to get your images from.
   If so, add a line like this (changing the path if necessary; see [the Sphinx
   docs](http://sphinx-doc.org/config.html?highlight=static#confval-html_static_path)):

   ```python
   html_static_path = ['_static']
   ```

1. Add one more section to `conf.py` setting one or more theme options, like in
   this example (*note*: snippet doesn't include all possible options, see
   following list!):

   ```python
   html_theme_options = {
       'logo': 'logo.png',
       'github_user': 'bitprophet',
       'github_repo': 'alabaster',
   }
   ```

   The available theme options (which are all optional) are as follows:

   **Variables and feature toggles**

   * `logo`: Relative path (from `$PROJECT/_static/`) to a logo image, which
   will appear in the upper left corner above the name of the project.
      * If `logo` is not set, your `project` name setting (from the top level
      Sphinx config) will be used in a text header instead. This preserves a
      link back to your homepage from inner doc pages.
   * `logo_name`: Set to `true` to insert your site's `project` name under the
   logo image as text. Useful if your logo doesn't include the project name
   itself. Defaults to `false`.
   * `logo_text_align`: Which CSS `text-align` value to use for logo text (if
   there is any.)
   * `description`: Text blurb about your project, to appear under the logo.
   * `github_user`, `github_repo`: Used by `github_button` and `github_banner`
   (see below); does nothing if both of those are set to `false`.
   * `github_button`: `true` or `false` (default: `true`) - whether to link to
   your Github.
       * If `true`, requires that you set `github_user` and `github_repo`.
       * See also these other related options, which behave as described
   in [Github Buttons' README](https://github.com/mdo/github-buttons#usage):
          * `github_button_type`: Defaults to `watch`.
          * `github_button_count`: Defaults to `true`.
   * `github_banner`: `true` or `false` (default: `false`) - whether to apply a
   'Fork me on Github' banner in the top right corner of the page.
       * If `true`, requires that you set `github_user` and `github_repo`.
   * `travis_button`: `true`, `false` or a Github-style `"account/repo"`
   string - used to display a Travis-CI build status button in the sidebar. If
   `true`, uses your `github_(user|repo)` settings; defaults to `false.`
   * `gratipay_user`: Set to your [Gratipay](https://gratipay.com) username if
   you want a Gratipay 'Donate' section in your sidebar.
      * This used to be `gittip_user` before that service changed its name to
      Gratipay; we've left the old setting in place as an alias for backwards
      compatibility reasons. It may be removed in the future.
      * If both options are given, `gratipay_user` wins.
   * `analytics_id`: Set to your [Google
   Analytics](http://www.google.com/analytics/) ID (e.g. `UA-#######-##`) to
   enable tracking.
   * `touch_icon`: Path to an image (as with `logo`, relative to
   `$PROJECT/_static/`) to be used for an iOS application icon, for when pages
   are saved to an iOS device's home screen via Safari.
   * `extra_nav_links`: Dictionary mapping link names to link targets; these
   will be added in a UL below the main sidebar navigation (provided you've
   enabled `navigation.html`.) Useful for static links outside your Sphinx
   doctree.
   * `sidebar_includehidden`: Boolean determining whether the TOC sidebar
   should include hidden Sphinx toctree elements. Defaults to `true` so you can
   use `:hidden:` in your index page's root toctree & avoid having 2x copies of
   your navigation on your landing page.
   * `show_powered_by`: Boolean controlling display of the `Powered by Sphinx
   N.N.N. & Alabaster M.M.M` section of the footer. When True, is displayed
   next to the copyright information; when False, is hidden.

   **Style colors**

   These should be fully qualified CSS color specifiers such as `#004B6B` or
   `#444`. The first few items in the list are "global" colors used as defaults
   for many of the others; update these to make sweeping changes to the
   colorscheme. The more granular settings can be used to override as needed.

   * `gray_1`: Dark gray.
   * `gray_2`: Light gray.
   * `gray_3`: Medium gray.
   * `body_text`: Main content text.
   * `footer_text`: Footer text (includes links.)
   * `link`: Non-hovered body links.
   * `link_hover`: Body links, hovered.
   * `sidebar_header`: Sidebar headers. Defaults to `gray_1`.
   * `sidebar_text`: Sidebar paragraph text.
   * `sidebar_link`: Sidebar links (there is no hover variant.) Applies to both
   header & text links. Defaults to `gray_1.
   * `sidebar_link_underscore`: Sidebar links' underline (technically a
   bottom-border.)
   * `sidebar_search_button`: Background color of the search field's 'Go'
   button.
   * `sidebar_list`: Foreground color of sidebar list bullets & unlinked text.
   * `sidebar_hr`: Color of sidebar horizontal rule dividers. Defaults to
   `gray_3`.
   * `anchor`: Foreground color of section anchor links (the 'paragraph' symbol
   that shows up when you mouseover page section headers.)
   * `anchor_hover_fg`: Foreground color of section anchor links (as above)
   when moused over. Defaults to `gray_1.
   * `anchor_hover_bg`: Background color of above.
   * `note_bg`: Background of `.. note::` blocks. Defaults to `gray_2`.
   * `note_border`: Border of same.
   * `footnote_bg`: Background of footnote blocks.
   * `footnote_border`: Border of same. Defaults to `gray_2`.
   * `pre_bg`: Background of preformatted text blocks (including code
   snippets.) Defaults to `gray_2`.
   * `narrow_sidebar_bg`: Background of 'sidebar' when narrow window forces it
   to the bottom of the page.
   * `narrow_sidebar_fg`: Text color of same.
   * `narrow_sidebar_link`: Link color of same. Defaults to `gray_3`.

## Additional info / background

* [Fabric #419](https://github.com/fabric/fabric/issues/419) contains a lot of
  general exposition & thoughts as I developed Alabaster, specifically with a
  mind towards using it on two nearly identical 'sister' sites (single-version
  www 'info' site & versioned API docs site).
* Alabaster includes/requires a tiny Sphinx extension on top of the theme
  itself; this is just so we can inject dynamic metadata (like Alabaster's own
  version number) into template contexts. It doesn't add any additional
  directives or the like, at least not yet.
