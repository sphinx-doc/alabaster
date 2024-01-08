from datetime import datetime

extensions = [
    "sphinx.ext.extlinks",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "Alabaster"
copyright = f"{datetime.now().year} Jeff Forcier"

exclude_patterns = ["_build"]

extlinks = {
    "git_tag": ("https://github.com/sphinx-doc/alabaster/tree/%s", "%s"),
    "bug": ("https://github.com/sphinx-doc/alabaster/issues/%s", "#%s"),
    "feature": ("https://github.com/sphinx-doc/alabaster/issues/%s", "#%s"),
    "issue": ("https://github.com/sphinx-doc/alabaster/issues/%s", "#%s"),
}

html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "A light, configurable Sphinx theme",
    "github_user": "sphinx-doc",
    "github_repo": "alabaster",
    "fixed_sidebar": True,
    "tidelift_url": "https://tidelift.com/subscription/pkg/pypi-alabaster?utm_source=pypi-alabaster&utm_medium=referral&utm_campaign=docs",  # noqa
}
