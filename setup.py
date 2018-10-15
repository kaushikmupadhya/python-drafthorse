from codecs import open
from os import path

from sepadd import version
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

try:
    # Get the long description from the relevant file
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='sepadd',
    version=version,
    description='Python SEPA Direct Debit XML implementation',
    long_description=long_description,
    url='https://github.com/raphaelm/python-sepadd',
    author='Raphael Michel',
    author_email='mail@raphaelmichel.de',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='xml banking sepa',
    install_requires=[
    ],

    packages=find_packages(include=['sepadd', 'sepadd.*']),
)