from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='project-firewatch',
      version='0.0.1',
      description=u"Skeleton of a Python package",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Seth Wahle",
      author_email='osteth@gmail.com',
      url='https://github.com/ostet/project-firewatch',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
		  'flask',
		  'flask_api',
		  'flask_googlemaps',
		  'wget'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      projectfirewatch=projectfirewatch.scripts.cli:cli
      """
      )
