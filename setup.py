# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='transmogrify.nitf',
      version=version,
      description="A transmogrifier pipeline to convert Plone's news items in collective.nitf's news articles",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Plone :: 4.1",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
      keywords='plone transmogrifier nitf',
      author='Héctor Velarde',
      author_email='hector.velarde@gmail.com',
      url='https://github.com/hvelarde/transmogrify.nitf',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['transmogrify'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'collective.nitf',
        'collective.transmogrifier',
        'plone.app.transmogrifier',
        ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
