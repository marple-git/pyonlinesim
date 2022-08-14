project = 'pyonlinesim'
copyright = '2022, Marple'
author = 'Marple'
release = '1.0.1'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'furo'
html_logo = '_static/logo_black.svg'
html_static_path = ['_static']

source_suffix = '.rst'
master_doc = 'index'
