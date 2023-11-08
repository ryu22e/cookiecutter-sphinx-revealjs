import shutil
from pathlib import Path

sphinx_extensions_dir = Path("sphinx_extensions")
if "{{ cookiecutter.enable_budoux }}" == "y":
    file_name = "sphinx_budoux.py"
    ext_dir = Path("source") / "_ext"
    ext_dir.mkdir()
    ext_path = ext_dir / file_name
    source_path = sphinx_extensions_dir / file_name

    shutil.copyfile(source_path, ext_path)
shutil.rmtree(sphinx_extensions_dir)

if "{{ cookiecutter.enable_robots_txt }}" != "y":
    robots_txt_path = Path("source") / "robots.txt"
    robots_txt_path.unlink()

if "{{ cookiecutter.enable_favicon }}" != "y":
    favicon_path = Path("source") / "favicon.ico"
    favicon_path.unlink()

if "{{ cookiecutter.disable_title_uppercase }}" != "y":
    css_path = Path("source") / "_static" / "css" / "title_uppercase.css"
    css_path.unlink()

license = "{{ cookiecutter.license }}"
licenses_dir = Path("licenses")
if license == "CC BY 4.0":
    license_path = licenses_dir / "CC-BY-4.0"
    shutil.copyfile(license_path, Path.cwd() / "LICENSE")
shutil.rmtree(licenses_dir)
