from setuptools import setup, find_packages

setup(
    name="simple-math-calculator",
    version="0.1.5",
    author="Albert",
    description="Fluent interface calculator",
    long_description="A simple flow-based calculator project",
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.8',
)