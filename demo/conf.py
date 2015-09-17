import alabaster

extensions = [
    'alabaster'
]

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

project = 'Demo'
copyright = '2015, My Name'
author = 'My Name'

version = 'X.Y.Z'

language = 'en'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'alabaster'

html_theme_options = {
    'github_user': 'bitprophet',
    'github_repo': 'alabaster',
    'github_banner': True,
    'travis_button': True,
    'show_powered_by': True
}
html_theme_path = [alabaster.get_path()]
html_static_path = []
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html'
    ]
}
