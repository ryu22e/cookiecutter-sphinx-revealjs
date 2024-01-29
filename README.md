# cookiecutter-sphinx-revealjs
Cookiecutter Template for sphinx-revealjs.

## Usage
```shell
$ cookiecutter https://github.com/ryu22e/cookiecutter-sphinx-revealjs
  [1/13] project_name (cookiecutter sphinx revealjs):
  [2/13] project_slug (cookiecutter-sphinx-revealjs):
  [3/13] title (Example):
  [4/13] copyright_year (2024):
  [5/13] author_name (Ryuji Tsutsui):
  [6/13] release (1.0):
  [7/13] language (ja):
  [8/13] enable_budoux (y):
  [9/13] enable_robots_txt (y):
  [10/13] enable_favicon (y):
  [11/13] disable_title_uppercase (n):
  [12/13] Select revealjs_style_theme
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
  [13/13] Select license
    1 - CC BY 4.0
    2 - None
    Choose from [1/2] (1):
$ cd cookiecutter-sphinx-revealjs
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ make revealjs
(.venv)$ ls build/revealjs
_sources    _static     favicon.ico index.html  objects.inv robots.txt
```

## Setting up GitHub Pages
![Setting up GitHub Pages](./img/setting-up-github-pages.jpg "Setting up GitHub Pages")
