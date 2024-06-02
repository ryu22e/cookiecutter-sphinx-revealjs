# cookiecutter-sphinx-revealjs

GitHub Repository URL: <https://github.com/ryu22e/cookiecutter-sphinx-revealjs>

## What is this?
A cookiecutter template for using [sphinx-revealjs](https://sphinx-revealjs.readthedocs.io/en/stable/).

## Features
- A template suitable for creating presentation materials for IT communities
- Supports Japanese word segmentation
- Supports Markdown notation


## How to Use
### Required Environment
- Python 3.9 or later
- [cookiecutter](https://pypi.org/project/cookiecutter/) 2.0.0 or later

### Creation Procedure
```revealjs-code-block:: bash

$ cookiecutter https://github.com/ryu22e/cookiecutter-sphinx-revealjs
(follow the prompts to complete the setup)
$ cd cookiecutter-sphinx-revealjs
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ make revealjs
(.venv)$ ls build/revealjs
_sources    _static     favicon.ico index.html  objects.inv robots.txt

```
