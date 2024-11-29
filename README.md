# cookiecutter-sphinx-revealjs
Cookiecutter Template for sphinx-revealjs.

## Usage
```shell
$ cookiecutter https://github.com/ryu22e/cookiecutter-sphinx-revealjs
$ cd cookiecutter-sphinx-revealjs
  [1/15] project_name (cookiecutter sphinx revealjs):
  [2/15] project_slug (cookiecutter-sphinx-revealjs):
  [3/15] title (Example):
  [4/15] Select python_version
    1 - 3.13
    2 - 3.12
    3 - 3.11
    4 - 3.10
    Choose from [1/2/3/4] (1):
  [5/15] copyright_year (2024):
  [6/15] author_name (Ryuji Tsutsui):
  [7/15] release (1.0):
  [8/15] language (ja):
  [9/15] enable_budoux (y):
  [10/15] enable_robots_txt (y):
  [11/15] enable_favicon (y):
  [12/15] disable_title_uppercase (n):
  [13/15] Select style
    1 - reStructuredText
    2 - Markdown
    Choose from [1/2] (1):
  [14/15] Select revealjs_style_theme
    1 - black
    2 - white
    3 - league
    4 - beige
    5 - sky
    6 - night
    7 - serif
    8 - simple
    9 - solarized
    10 - blood
    11 - moon
    Choose from [1/2/3/4/5/6/7/8/9/10/11] (1):
  [15/15] Select license
    1 - CC BY 4.0
    2 - None
    Choose from [1/2] (1):
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ make revealjs
(.venv)$ ls build/revealjs
_sources    _static     favicon.ico index.html  objects.inv robots.txt
```

## Setting up GitHub Pages
![Setting up GitHub Pages](./img/setting-up-github-pages.jpg "Setting up GitHub Pages")
