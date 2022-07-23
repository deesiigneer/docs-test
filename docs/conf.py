from re import search, MULTILINE

project = 'pyspapi-docs-test'
copyright = '2022, deesiigneer'
author = 'deesiigneer'
with open("../pyspapi/__init__.py") as f:
    match = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), MULTILINE)

    if not match or match.group(1) is None:
        raise RuntimeError("The version could not be resolved")

    version = match.group(1)

# The full version, including alpha/beta/rc tags.
release = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
language = None
locale_dirs = ["locale/"]
exclude_patterns = []
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/deesiigneer/pyspapi",
            "icon": "fab fa-brands fa-github",
            "type": "fontawesome"
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/VbyHaKRAaN",
            "icon": "fab fa-brands fa-discord",
            "type": "fontawesome"
        },
        {
            "name": "PyPi",
            "url": "https://pypi.org/project/pyspapi/",
            "icon": "fab fa-brands fa-python",
            "type": "fontawesome"
        }
  ],
    "use_edit_page_button": True
}
html_context = {
    "github_user": "deesiigneer",
    "github_repo": "pyspapi",
    "github_version": "main",
    "doc_path": "https://github.com/deesiigneer/pyspapi/tree/main/docs",
}