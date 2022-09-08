# -*- coding: utf-8 -*-
"""
Alternating text and code
=========================

Sphinx-Gallery is capable of transforming Python files into rST files
with a notebook structure. For this to be used you need to respect some syntax
rules. This example demonstrates how to alternate text and code blocks and some
edge cases. It was designed to be compared with the
:download:`source Python script <plot_parse.py>`."""


# %%
# This is the first text block and directly follows the header docstring above.

import numpy as np

# %%

# You can separate code blocks using either a single line of ``#``'s
# (>=20 columns), ``#%%``, or ``# %%``. For consistency, it is recommend that
# you use only one of the above three 'block splitter' options in your project.
A = 1

import matplotlib.pyplot as plt

