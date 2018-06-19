from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gunicorn-logging',
    version='0.1.0',
    description='Gunicorn centralized logging',
    long_description=long_description,
    url='https://github.com/emilioag/gunicorn-logging/',
    author='emilioag',
    author_email='emilioag@mail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django, logging, gunicorn, logstash, elk',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[
        'python-json-logger==0.1.9',
        'python-logstash-async==1.4.1'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)