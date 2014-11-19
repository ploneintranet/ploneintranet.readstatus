# -*- coding: utf-8 -*-
"""Installer for the ploneintranet.readstatus package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='ploneintranet.readstatus',
    version='0.1',
    description="""Plone Intranet "Must Read" feature""",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone, ploneintranet',
    author='Eric BREHAULT',
    author_email='ebrehault@gmail.com',
    url='http://pypi.python.org/pypi/ploneintranet.readstatus',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneintranet'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'plone.behavior',
        'plone.directives.form',
        'zope.schema',
        'zope.interface',
        'zope.component',
        'rwproperty',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'plone.reload',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
