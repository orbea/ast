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

project = 'Korn Shell'
copyright = '2019, David J. Korn, et.al.'
author = 'David J. Korn, et.al.'

# The full version, including alpha/beta/rc tags
release = '2020.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
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
# html_theme = 'classic'
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Control which documents get converted to man pages by `make man`.
man_pages = [
    # Builtin commands.
    ('alias', 'alias', 'define or display aliases',
     'David J. Korn, et. al.', '1'),
    ('bg', 'bg', 'resume jobs in the background',
     'David J. Korn, et. al.', '1'),
    ('break', 'break', 'break out of loop',
     'David J. Korn, et. al.', '1'),
    ('builtin', 'builtin', 'add, delete, or display shell built-ins',
     'David J. Korn, et. al.', '1'),
    ('cd', 'cd', 'change working directory',
     'David J. Korn, et. al.', '1'),
    ('command', 'command', 'execute a simple command',
     'David J. Korn, et. al.', '1'),
    ('continue', 'continue', 'continue execution at top of the loop',
     'David J. Korn, et. al.', '1'),
    ('disown', 'disown', 'disassociate a job from the current shell',
     'David J. Korn, et. al.', '1'),
    ('echo', 'echo', 'output a line of text',
     'David J. Korn, et. al.', '1'),
    ('enum', 'enum', 'create an enumeration type',
     'David J. Korn, et. al.', '1'),
    ('eval', 'eval', 'create a shell command and process it',
     'David J. Korn, et. al.', '1'),
    ('exec', 'exec', 'execute command, open/close/duplicate file descriptors',
     'David J. Korn, et. al.', '1'),
    ('exit', 'exit', 'exit the current shell',
     'David J. Korn, et. al.', '1'),
    ('export', 'export', 'set export attribute on variables',
     'David J. Korn, et. al.', '1'),
    ('fg', 'fg', 'move jobs to the foreground',
     'David J. Korn, et. al.', '1'),
    ('hist', 'hist', 'move jobs to the foreground',
     'David J. Korn, et. al.', '1'),
    ('source', 'source', 'execute commands in the current environment',
     'David J. Korn, et. al.', '1'),
    # External commands available as builtins.
    ('basename', 'basename', 'strip directory and suffix from filenames',
     'David J. Korn, et. al.', '1'),
    ('cat', 'cat', 'concatenate files',
     'David J. Korn, et. al.', '1'),
    ('chmod', 'chmod', 'change the access permissions of files',
     'David J. Korn, et. al.', '1'),
    ('cmp', 'cmp', 'compare two files',
     'David J. Korn, et. al.', '1'),
    ('cut', 'cut', 'cut out selected columns or fields of each line of a file',
     'David J. Korn, et. al.', '1'),
    ('dirname', 'dirname', 'return directory portion of file name',
     'David J. Korn, et. al.', '1'),
    ('head', 'head', 'output beginning portion of one or more files',
     'David J. Korn, et. al.', '1'),
]
