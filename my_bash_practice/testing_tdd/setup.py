from setuptools import setup, find_packages

setup(
    name = "ndfl-alb",
    version = "0.0.0",
    long_description = "Makefile",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author = "Albert Ananyan"
)