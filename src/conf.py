from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions

project = 'f-utils'
copyright = '2025, Yuri Ximenes'
author = 'Yuri Ximenes'

extensions = []

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
pygments_style_dark = "github-dark"
pygments_style = "xcode"
html_permalinks_icon = "<span>#</span>"

theme_options = ThemeOptions(
    show_breadcrumbs=True,
    main_nav_links={
        "about": "/about",
        "docs": "/docs",
        "libs": "/libs"
    },
    extra_header_link_icons={
        "github": {
            "icon": "_static/github.svg",
            "link": "https://github.com/f-utils"
            }
    },
    awesome_headerlinks=True,
    show_prev_next=True,
)

html_theme_options = asdict(theme_options)

