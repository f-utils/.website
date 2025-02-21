# install

In this documentation we talk about the installation process of `f-utils` libs.

## branches

Recall that the `f-utils` libs correspond to repositories in the [f-utils](https://github.com/f-utils) organization, named under `f-{lib}`. Their installation is directly from certain branches in their corresponding repository:
1. `main`: the stable version of the lib
2. `dev`: a new version in development.

##  agnostics

The libs are _package manager agnostics_, which means that you can install them from your favorite method. Below we list some examples.

- With `git`:
```bash
# main branch
git clone https://github.com/f-utils/f-{lib} /path/to/venv/lib/python-3.x/site-packages/f-{lib}
# dev branch
git clone https://github.com/f-utils/f-{lib}/tree/dev /path/to/venv/lib/python-3.x/site-packages/f-{lib}
```

- With `pip`:
```bash
# main branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-{lib}
# dev branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-{lib}/tree/dev
```

- With [poetry](https://python-poetry.org/):
```bash
# main branch
poetry add git+https://github.com/f-utils/f-{lib}
# dev branch
poetry add git+https://github.com/f-utils/f-{lib}/tree/dev
```

- With [uv](https://github.com/astral-sh/uv):
```bash
# main branch
uv add git+https://github.com/f-utils/f-{lib}
# dev branch
uv add git+https://github.com/f-utils/f-{lib} --branch dev
```

- With [pdm](https://pdm-project.org/en/latest/):
```bash
# main branch
pdm add git+https://github.com/f-utils/f-{lib}
# dev branch
pdm add git+https://github.com/f-utils/f-{lib}/tree/dev
```

- With [py](https://github.com/ximenesyuri/py):
```bash
# main branch
py install f-utils/f-{lib} --from github
# dev branch
py install f-utils/f-{lib} --from github --branch dev
```
