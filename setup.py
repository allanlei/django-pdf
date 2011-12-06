from distutils.core import setup
from setuptools import find_packages
import os
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-pdf',
    version = '0.1.1',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = ('PDF utilities for Django'),
    license = 'New BSD',
    keywords = 'pdf utils django',
    url = 'https://github.com/allanlei/django-pdf',
    packages=find_packages_in('djpdf'),
    long_description=read('README'),
    install_requires=[
#        'pisa>=3.0.33',
#        'html5lib==0.90',       pisa
#        'reportlab==2.5',       pisa
#        'pdfkit=='
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
