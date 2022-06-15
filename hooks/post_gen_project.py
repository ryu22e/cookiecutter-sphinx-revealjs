import shutil
from pathlib import Path

if "{{ cookiecutter.enable_budoux }}" == "y":
    file_name = "sphinx_budoux.py"
    ext_dir = Path("source") / "_ext"
    ext_dir.mkdir()
    ext_path = ext_dir / file_name
    source_dir = Path("sphinx_extensions")
    source_path = source_dir / file_name

    shutil.copyfile(source_path, ext_path)
    shutil.rmtree(source_dir)

if "{{ cookiecutter.enable_robots_txt }}" != "y":
    robots_txt_path = Path("source") / "robots.txt"
    robots_txt_path.unlink()
