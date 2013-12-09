# Modified 'Kr/Flask' Sphinx theme

This repository is a modified "Kr" Sphinx theme from @kennethreitz (especially
as used in his [Requests](https://python-requests.org) project), which was in
turn modfied from @mitsuhiko's theme used for [Flask](http://flask.pocoo.org/)
& related projects.

I named the theme itself back to "flasky" (reflecting that it's relatively
generic and not used for Kenneth's own projects, but my own or anybody else's
use) and tried to polish it up. To wit, changes from Kenneth's theme:

* No 'small' theme since I didn't need it & wanted to remove noise;
* Minor style tweaks, such as ensuring code blocks left-align with regular text
  blocks (in Kenneth's theme they are dedented too far);
* Additional customization hooks, such as header/link/etc colors;
* Improved documentation for all customizations (pre-existing & new).

To use:

1. Use this folder as the `_themes` subdirectory of your Sphinx project (copy
   it, use a git submodule, whatever.)
1. Enable the 'flasky' theme in your `conf.py`:

   ```python
   import os
   import sys
   
   sys.path.append(os.path.abspath('_themes'))
   html_theme_path = ['_themes']
   html_theme = 'flasky'
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

1. If desired, add a final option to `conf.py` overriding one or more theme
   options, like in this example (*note*: snippet doesn't include all possible
   options, see following list!):

   ```python
   html_theme_options = {
       'logo': 'static/logo.png',
       'github_user': 'bitprophet',
       'github_repo': 'sphinx-theme',
   }
   ```

   The available theme options (which are all optional) are as follows:

   * `logo`: Relative path (from `$PROJECT/_themes/`) to a logo image, which
   will appear in the upper left corner above the name of the project.
       * **Note:** while this is technically optional, things will look
       slightly off without one. We recommend coming up with a logo and making
       it approximately 224x200 pixels. See e.g.
       [Requests](http://docs.python-requests.org/en/latest/_static/requests-sidebar.png).
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
   * `touch_icon`: Path to an image to be used for an iOS application icon, for
   when pages are saved to an iOS device's home screen via Safari.
