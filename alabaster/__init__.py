import os

__version_info__ = (0, 7, 14)
__version__ = "0.7.14"

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["alabaster_version"] = __version__
    # either use 'show_powered_by' when specified in 'html_theme_options'
    # or the top-level configuration value 'html_show_sphinx' directly
    html_theme_options = app.config.html_theme_options
    if 'show_powered_by' in html_theme_options:
        show_powered_by = html_theme_options['show_powered_by']
        if isinstance(show_powered_by, str):
            show_powered_by = show_powered_by.lower() == 'true'
    else:
        show_powered_by = context['show_sphinx']
    show_powered_by = bool(show_powered_by)  # to allow int values
    # keep `theme_show_powered_by` flag for backward compatibility
    context['show_sphinx'] = context['theme_show_powered_by'] = show_powered_by


def setup(app):
    app.require_sphinx("3.4")
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("alabaster", theme_path)
    app.connect("html-page-context", update_context)
    return {"version": __version__, "parallel_read_safe": True}
