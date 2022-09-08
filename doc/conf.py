# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'BEP032-examples'
copyright = '2022, Julia Sprenger'
author = 'Julia Sprenger'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx_gallery.gen_gallery',
    'myst_parser'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Sphinx gallery project configuration
sphinx_gallery_conf = {
    'examples_dirs': '../tutorials',  # path to your example scripts
    'gallery_dirs': 'auto_tutorials',  # path to where to save gallery generated output
    'show_memory': True,
    'line_numbers': True,
    'ignore_pattern': r'in_container_sorter_script\.py',
    'binder': {
         # Required keys
         'org': 'juliasprenger',
         'repo': 'BEP032-doc',  # link to github repository
         'branch': 'add/doc', # Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
         'binderhub_url': 'https://mybinder.org', # Any URL of a binderhub deployment. Must be full URL (e.g. https://mybinder.org).
         'dependencies': '../tutorials/environment.yml',
         # Optional keys
         'filepath_prefix': '',  # A prefix to prepend to any filepaths in Binder links.
         'notebooks_dir': 'doc',  # Jupyter notebooks for Binder will be copied to this directory (relative to built documentation root).
         'use_jupyter_lab': False  # Whether Binder links should start Jupyter Lab instead of the Jupyter Notebook interface.
    }
}
