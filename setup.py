import setuptools
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(name='gem_tools',
      version='0.0.1',
      description='Tools for working with multimodal corpora annotated using the Genre and Multimodality model',
      url='https://github.com/thiippal/gem-tools',
      author='Tuomo Hiippala',
      packages=['gem_tools'],
      package_dir={'gem_tools': 'gem_tools'},
      package_data={'gem_tools': ['*.pkl', 'model/*.pkl', '*.ipynb', '*.ipynb']},
      author_email='tuomo.hiippala@helsinki.fi',
      license='MIT',
      keywords=['multimodality', 'imaging', 'ocr'],
      # add current versions?
      install_requires=["graphviz>=0.4.10",
                        "cv2",
                        "mahotas",
                        "numpy",
                        "imutils",
                        "pytesser",
                        "nltk",
                        "vlogging",
                        "skimage",
                        "sklearn"])
