import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "weathervane",
    version = "0.0.1",
    author = "Group1 Enterprises",
    author_email = "adanter@gmail.com",
    description = ("Application that provides helpful weather info "
                                   "for trip planning."),
    license = "MIT",
    keywords = "weather travel",
    url = "http://packages.python.org/weathervane",
    packages=['weathervane', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Flask",
        "Intended Audience :: Education",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
    ],
)
