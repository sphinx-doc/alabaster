# Alabaster: a Sphinx theme

This theme is a modified "Kr" Sphinx theme from @kennethreitz (especially as
used in his [Requests](https://python-requests.org) project), which was itself
originally based on @mitsuhiko's theme used for
[Flask](http://flask.pocoo.org/) & related projects.

Features (compared to Kenneth's theme):

* Easy ability to install/use as a Python package (tip o' the hat to [Dave &
  Eric's sphinx_rtd_theme](https://github.com/snide/sphinx_rtd_theme) for
  showing the way);
* Minor style tweaks, such as better code-block alignment, Gittip button
  placement, etc;
* Additional customization hooks, such as header/link/etc colors;
* Improved documentation for all customizations (pre-existing & new).

To use:

1. `pip install alabaster` (or equivalent command)
1. Enable the 'alabaster' theme in your `conf.py`:

   ```python
   import alabaster

   html_theme_path = [alabaster.get_path()]
   html_theme = 'alabaster'
   html_sidebars = {
       'index': [
           'sidebar.html', 'sourcelink.html', 'searchbox.html'
       ],
       '**': [
           'sidebar.html', 'localtoc.html', 'relations.html',
           'sourcelink.html', 'searchbox.html'
       ]
   }
   ```

    * Modify the call to `abspath` if your `_themes` folder doesn't live right
    next to your `conf.py`.
    * Feel free to adjust `html_sidebars` as desired - the theme is designed
    assuming you'll have `sidebar.html` activated, but otherwise it doesn't
    care much.
        * See [the Sphinx
        docs](http://sphinx-doc.org/config.html#confval-html_sidebars) for
        details on how this setting behaves.
        * The theme ships with a modified (improved, sidebar & complex doctree
        friendly) `relations.html` as well, but does not require that you
        enable it.

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
   * `gittip_user`: Set to your [Gittip](https://gittip.com) username if you
   want a Gittip 'Donate' section in your sidebar.
   * `analytics_id`: Set to your [Google
   Analytics](http://www.google.com/analytics/) ID (e.g. `UA-#######-##`) to
   enable tracking.
   * `touch_icon`: Path to an image (as with `logo`, relative to
   `$PROJECT/_static/`) to be used for an iOS application icon, for when pages
   are saved to an iOS device's home screen via Safari.

   **Style colors**

   These should be fully qualified CSS color specifiers such as `#004B6B` or
   `#444`:

   * `body_text`: Main content text.
   * `footer_text`: Footer text (includes links.)
   * `link`: Non-hovered body links.
   * `link_hover`: Body links, hovered.
   * `sidebar_header`: Sidebar headers.
   * `sidebar_text`: Sidebar paragraph text.
   * `sidebar_link`: Sidebar links (there is no hover variant.) Applies to both
   header & text links.
   * `sidebar_link_underscore`: Sidebar links' underline (technically a
   bottom-border.)
   * `sidebar_search_button`: Background color of the search field's 'Go'
   button.
   * `sidebar_list`: Foreground color of sidebar list bullets & unlinked text.
   * `anchor`: Foreground color of section anchor links (the 'paragraph' symbol
   that shows up when you mouseover page section headers.)
   * `anchor_hover_fg`: Foreground color of section anchor links (as above)
   when moused over.
   * `anchor_hover_bg`: Background color of above.
   * `note_bg`: Background of `.. note::` blocks
   * `note_border`: Border of same.
   * `footnote_bg`: Background of footnote blocks.
   * `footnote_border`: Border of same.
