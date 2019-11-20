from setuptools import setup

setup(name='fallbeyging',
      version='1.0',
      description='',
      url='https://github.com/slowpokesheep/fallbeyging',
      author='Flying Circus',
      scripts=['bin/fallbeyging'],
      packages=['fallbeyging'],
      install_requires=[
          'pygame',
      ],
      zip_safe=False)