from setuptools import setup, find_packages

from polybar_onlinestatus import __version__ as version

# META DATA
__author__ = "sTiKyt"
__version__ = version
__package_name__ = "polybar_onlinestatus"
__description__ = "Polybar module to check if you are online"
__python_requires__ = ">=3.6.*"
__url__ = "https://github.com/sTiKyt/polybar-onlinestatus"

with open("README.md", "r") as readme:
    __long_description__ = readme.read()

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    description=__description__,
    python_requires=__python_requires__,
    url=__url__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            'polybar-onlinestatus = polybar_onlinestatus.polybar_onlinestatus:main'
        ]
    }

)
