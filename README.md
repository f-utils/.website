# About

This is the repository of `f-utils` webpage, made with [sphinx](https://www.sphinx-doc.org/en/master/index.html).

# Structure

```
.website/
  |-- src/ ............... .rst files and conf.py
  `-- dist/ .............. generated static files
```

# Install

1. Clone this repository
2. Create a `.venv`
3. Install the `requirements.txt`

# Build

1. Activate the `.venv`
2. Execute `make html`.

# Flow

While pushing to the `main` the runner make the build and update the `gh-pages` branch with `dist/html`, which is displayed with Github Pages.
