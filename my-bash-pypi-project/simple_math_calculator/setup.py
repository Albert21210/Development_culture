from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-math-calculator",
    version="0.1.2",
    author="Albert",
    description="A fluent calculator for basic arithmetic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Albert21210/Development_culture",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[], 
)