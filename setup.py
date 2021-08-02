from setuptools import setup
import sys
import re


with open("README.rst") as readme_file:
    readme_text = readme_file.read()

VERSIONFILE = "geojson/_version.py"
verstrline = open(VERSIONFILE).read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSIONFILE}.")


def test_suite():
    import doctest
    import unittest

    suite = unittest.TestLoader().discover("tests")
    suite.addTest(doctest.DocFileSuite("README.rst"))
    return suite


major_version, minor_version = sys.version_info[:2]
if not (major_version == 3 and 9 <= minor_version <= 10):
    sys.stderr.write("Sorry, only Python 3.9 - 3.10 are "
                     "supported at this time.\n")
    exit(1)

setup(
    name="MapUI",
    version=verstr,
    description="MapUI using Python bindings and utilities for GeoJSON",
    license="BSD",
    keywords="gis geography json",
    author="adamin",
    author_email="adamin@launchlabs.dev",
    maintainer="adamin",
    maintainer_email="adamin@launchlabs.dev",
    url="https://github.com/jazzband/geojson",
    long_description=readme_text,
    packages=["geojson"],
    package_dir={"geojson": "geojson"},
    package_data={"geojson": ["*.rst"]},
    install_requires=[],
    test_suite="setup.test_suite",
    python_requires="<=3.9",
    classifiers=[
        "Development Status :: 1 - Development/Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: GIS",
    ]
)
