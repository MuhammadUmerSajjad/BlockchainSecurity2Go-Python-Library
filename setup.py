from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
  name='blockchain-security2go-starterkit',
  version='0.1',
  author='Infineon Technologies AG',
  author_email='?',
  description='Allow for communication with the Infineon Blockchain Security2GO Starterkit',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='http://github.com/infineon/python-blockchain2go',
  license='MIT',
  packages=find_packages(),
  install_requires=[
    'pyscard'
  ],
  entry_points={
    'console_scripts': [
      'bc2go = blockchain2go.cli.main:main',
    ],
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  zip_safe=False
)