# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # Ajusta a la ruta donde tienes tus archivos Python

autodoc_default_options = {
    'members': False,            # Incluye todos los miembros (métodos y atributos)
    'undoc-members': True,      # Incluye miembros sin docstrings
    'show-inheritance': True,   # Muestra la herencia de clases
}


# -- Project information -----------------------------------------------------

project = 'Team1.'
copyright = '2024, Grupo1'
author = 'Grupo1'
release = 'V0'


# -- General configuration ---------------------------------------------------

# Extensions that add functionalities
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx'
  
]


# Intersphinx mapping to other projects' documentation (example)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Templates path
templates_path = ['_templates']

# Patterns to exclude from the build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# HTML theme (Alabaster, Sphinx's default theme, or another)


# Paths for static files (CSS, JavaScript)
#html_static_path = ['_static']

html_theme = "sphinx_material"
# Opciones adicionales para el tema

html_theme_options = {
    'nav_title': 'Options',
    'color_primary': 'green',
    'globaltoc_depth': 5,
}

# -- Options for Extensions --------------------------------------------------



# -- Additional Customization ------------------------------------------------

# Add any paths you need (e.g., src directory)
sys.path.insert(0, os.path.abspath('./src'))

