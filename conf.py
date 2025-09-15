# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any custom module paths if needed
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Your Lowe’s Credit Card'
copyright = '2025, Lowe’s'
author = 'Lowe’s & Synchrony Bank'

# Full version info
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in browser tab and at top of pages
html_title = "Activate Your Lowe’s Credit Card at lowes.syf.com/activate – Quick Guide"

# Optional short title
html_short_title = "Lowe’s Card Activation"

# Favicon (ensure you place favicon.ico in root or _static directory)
html_favicon = 'favicon.ico'

# Choose theme
# html_theme = 'sphinx_rtd_theme'  # Uncomment to use Read the Docs theme

# Hide “View page source” from UI
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to template files
templates_path = ['_templates']

# Uncomment if you use custom static files (e.g., styles, scripts)
# html_static_path = ['_static']

# Patterns to exclude during build
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
