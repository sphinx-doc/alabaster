Modified 'Kr/Flask' Sphinx theme
================================

This repository is a modified "Kr" Sphinx theme from @kennethreitz, which was
in turn modfied from @mitsuhiko's theme used for Flask & related projects.

I named the theme itself back to "flasky" (reflecting that it's relatively
generic and not used for Kenneth's own projects, but my own or anybody else's
use) and tried to polish it up. To wit, changes from Kenneth's theme:

* No 'small' theme since I didn't need it & wanted to remove noise;
* Additional customization hooks, such as header/link/etc colors;
* Improved documentation for all customizations (pre-existing & new).

To use:

1. Use this folder as the ``_themes`` subdirectory of your Sphinx project (copy
   it, use a git submodule, whatever.)
2. Add to your ``conf.py``::

    import os
    import sys

    sys.path.append(os.path.abspath('_themes'))
    html_theme_path = ['_themes']
    html_theme = 'flasky'

TK: documented customization hooks
