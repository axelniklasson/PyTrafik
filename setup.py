# -*- coding: utf-8 -*-
""" Setup for vasttrafik-api-wrapper """

from distutils.core import setup

setup(
    name='vasttrafik-api-wrapper',
    version='1.0.3',
    description='Västtrafik API wrapper.',
    long_description='Wrapper for Västtrafik public API.',
    url='https://github.com/axelniklasson/vasttrafik-api-wrapper',
    download_url = 'https://github.com/axelniklasson/vasttrafik-api-wrapper/tarball/1.0.3',
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
    packages=['vasttrafik-api-wrapper'],
    zip_safe=True)
