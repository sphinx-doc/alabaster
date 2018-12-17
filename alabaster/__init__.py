import os

try:
    import requests
except ImportError:
    pass

from alabaster import _version as version


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["alabaster_version"] = version.__version__

    set_up_travis_context(context)


def set_up_travis_context(context):
    """Add complete Travis URLs to Jinja2 context."""
    github_slug = "/".join(
        (context["theme_github_user"], context["theme_github_repo"])
    )

    travis_button = str(context["theme_travis_button"]).lower()
    travis_button_enabled = travis_button == "true"

    travis_slug = github_slug if travis_button_enabled else travis_button

    travis_tld = context["theme_travis_tld"].lower()
    if travis_button_enabled and travis_tld == "auto":
        try:
            travis_api_response = requests.get(
                "https://api.travis-ci.com/repo/{}".format(
                    travis_slug.replace("/", "%2F")
                ),
                headers={
                    "Travis-API-Version": "3",
                    "User-Agent": "Sphinx-Alabaster-Theme/{version} "
                    "(+https://github.com/bitprophet/alabaster)".format(
                        version=version.__version__
                    ),
                },
            )
            is_travis_com_repo = 200 <= travis_api_response.status_code < 300
            travis_tld = "com" if is_travis_com_repo else "org"
        except NameError:
            travis_tld = "com"
    elif travis_tld != "com":
        travis_tld = "org"
    travis_base_uri = "travis-ci.{}/{}".format(travis_tld, travis_slug)
    context["theme_travis_build_url"] = "https://{}".format(travis_base_uri)
    context["theme_travis_badge_url"] = "https://api.{}.svg?branch={}".format(
        travis_base_uri, context["theme_badge_branch"]
    )


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("alabaster", theme_path)
    app.connect("html-page-context", update_context)
    return {"version": version.__version__, "parallel_read_safe": True}
