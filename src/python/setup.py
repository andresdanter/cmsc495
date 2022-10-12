import os
from setuptools import setup

"""
Weather Vane Application
Course: CMSC495
Group 1
"""

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
