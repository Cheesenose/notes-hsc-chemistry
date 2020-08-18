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

project = "HSC Chemistry"
copyright = "2020"
author = "Modelmat"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "notfound.extension", # 404 page
    "sphinx.ext.mathjax", # math expressions
    "sphinx.ext.autosectionlabel", # easier to reference sections
    "sphinxext.opengraph", # url preview embed
    "hoverxref.extension", # hover glossary terms
]


# -- Extension Options --------------------------------------------------------
# Configure OpenGraph support
ogp_site_url = "https://hsc-chemistry.readthedocs.io"
ogp_site_name = "HSC Chemistry Notes"

# Enable hover content on glossary term
hoverxref_roles = ["term"]
hoverxref_mathjax = True

# Autosection labels prefix document path and filename
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "css/blockquote.css",
]

# -- Various Helper Bits -----------------------------------------------------
rst_epilog = """
.. |syllabus-nesa| replace:: --Chemistry Stage 6 Syllabus, NESA
.. _syllabus-nesa: https://educationstandards.nsw.edu.au/wps/portal/nesa/11-12/stage-6-learning-areas/stage-6-science/chemistry-2017
"""
