# {{ cookiecutter.title }}

## Requirements
* Git
* Python 3.9 or higher
* Your favorite editor

## How to Build
```bash
$ git clone {repository url}
$ cd {repository path}
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ vim source/index.md  # Replace vim with your favorite editor
(.venv)$ make revealjs  # Build to build/revealjs/
```
