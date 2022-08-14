import pyonlinesim

project = 'pyonlinesim'
copyright = '2022, Marple'
author = 'Marple'
release = pyonlinesim.__version__


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

rst_prolog = """
.. role:: pycode(code)
   :language: python3
"""

latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation', author, 'manual'),
]

man_pages = [(master_doc, project, f'{project} Documentation', [author], 1)]

texinfo_documents = [
    (
        master_doc,
        project,
        f'{project} Documentation',
        author,
        project,
        'Modern and fully asynchronous framework for Telegram Bot API',
        'Miscellaneous',
    ),
]