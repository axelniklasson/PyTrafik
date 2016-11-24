# -*- coding: utf-8 -*-
""" Setup for pytrafik """

from distutils.core import setup

setup(
    name='pytrafik',
    version='0.2',
    description='PyTrafik',
    long_description='Wrapper for Västtrafik public API.',
    url='https://github.com/axelniklasson/PyTrafik',
    download_url = 'https://github.com/axelniklasson/PyTrafik/tarball/0.2',
    author='Axel Niklasson',
    author_email='hello@axelniklasson.se',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='vasttrafik västtrafik',
    install_requires=['requests>=2.9.1'],
    packages=['pytrafik'],
    zip_safe=True)
