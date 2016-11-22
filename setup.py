# -*- coding: utf-8 -*-
""" Setup for vasttrafik-api-wrapper """

from distutils.core import setup

setup(
    name='vasttrafik',
    version='1.0.0',
    description='Västtrafik API.',
    long_description='Wrapper for Västtrafik public API.',
    url='https://github.com/axelniklasson/vasttrafik-api-wrapper',
    download_url = 'https://github.com/axelniklasson/vasttrafik-api-wrapper/tarball/1.0.0',
    author='Axel Niklasson',
    author_email='axel.niklasson@live.com',
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
    packages=['vasttrafik'],
    zip_safe=True)
