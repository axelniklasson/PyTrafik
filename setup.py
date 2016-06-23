""" Setup for vasttrafik-api-wrapper """

from setuptools import setup

setup(
    name='vasttrafik',
    version='0.1.0',
    description='Västtrafik API.',
    long_description='Wrapper for Västtrafik public API.',
    url='https://github.com/axelniklasson/vasttrafik-api-wrapper',
    author='Alex Niklasson',
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
