# cookiecutter-sphinx-revealjs
Cookiecutter Template for sphinx-revealjs.

## Usage
```shell
$ cookiecutter https://github.com/ryu22e/cookiecutter-sphinx-revealjs
project_name [cookiecutter sphinx revealjs]:
project_slug [cookiecutter-sphinx-revealjs]:
title [Example]:
copyright_year [2023]:
author_name [Ryuji Tsutsui]:
release [1.0]:
language [ja]:
enable_budoux [y]:
enable_robots_txt [y]:
enable_favicon [y]:
Select revealjs_style_theme:
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
Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 [1]:
Select license:
1 - CC BY 4.0
2 - None
Choose from 1, 2 [1]:
$ cookiecutter-sphinx-revealjs
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ make revealjs
(.venv)$ ls build/revealjs
_sources    _static     favicon.ico index.html  objects.inv robots.txt
```
