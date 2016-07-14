import setuptools
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(name='gem-tools',
      version='0.0.1',
      description='Tools for working with multimodal corpora annotated using the Genre and Multimodality model',
      url='https://github.com/thiippal/gem-tools',
      author='Tuomo Hiippala',
      packages=['gem-tools'],
      package_dir={'gem-tools': 'gem-tools'},
      package_data={'gem-tools': ['*.pkl', 'model/*.pkl', '*.ipynb', '*.ipynb']},
      author_email='tuomo.hiippala@helsinki.fi',
      license='MIT',
      keywords=['multimodality', 'imaging', 'ocr'],
      install_requires=["graphviz>=0.4.10"])
