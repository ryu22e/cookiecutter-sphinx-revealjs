{{ cookiecutter.title|rest_title0 }}

Requirements
------------

* Git
* Python 3.10 or higher
* Your favorite editor

How to Build
------------

.. code-block:: bash

    $ git clone {repository url}
    $ cd {repository path}
    $ python -m venv .venv
    $ source .venv/bin/activate
    (.venv)$ pip install -r requirements_dev.txt
    (.venv)$ playwright install --with-deps chromium
    (.venv)$ vim source/index.rst  # Replace vim with your favorite editor
    (.venv)$ make revealjs  # Build to build/revealjs/

If you want to automatically rebuild when changes are made, you can use `sphinx-autobuild`:

.. code-block:: bash

    (.venv)$ sphinx-autobuild source build/revealjs -b revealjs  # Serve at http://localhost:8000
