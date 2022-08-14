# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyonlinesim'
copyright = '2022, Marple'
author = 'Marple'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

htmlhelp_basename = project
html_theme_options = {}
html_theme = 'furo'
html_logo = '_static/logo_black.svg'
html_static_path = ['_static']

source_suffix = '.rst'
master_doc = 'index'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

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
        'Asynchronous wrapper to interact with onlinesim.ru API',
    ),
]
