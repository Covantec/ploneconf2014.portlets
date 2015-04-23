from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.portlets',
      version=version,
      description="Plone Portlets Custom for Ploneconf2014 Demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='ploneconf portlets plone custom Cantv.com.ve',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/Covantec/ploneconf2014.portlets',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
