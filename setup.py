#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "geopandas", "fiona", "rasterio", "shapely", "whitebox"]

setup_requirements = []

test_requirements = ["pytest>=3", "pytest-mpl"]

setup(
    author="Paul M. Hobson",
    author_email="phobson@geosyntec.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Iowa Ag BMP Assessor",
    entry_points={
        "console_scripts": [
            "iowa=iowag.cli:main",
            "bmp=iowag.cli:iowabmp",
            "dem=iowag.cli:iowadem",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="iowag",
    name="iowag",
    packages=find_packages(include=["iowag", "iowag.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/phobson/iowag",
    version="0.0.1",
    zip_safe=False,
)
