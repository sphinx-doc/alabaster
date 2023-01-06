import os

__version_info__ = (0, 7, 13)
__version__ = "0.7.13"


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["alabaster_version"] = __version__


def setup(app):
    app.require_sphinx("1.6")
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("alabaster", theme_path)
    app.connect("html-page-context", update_context)
    return {"version": __version__, "parallel_read_safe": True}
