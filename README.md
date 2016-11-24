# PyTrafik
[![PyPI version](https://badge.fury.io/py/PyTrafik.svg)](https://badge.fury.io/py/PyTrafik)
[![GitHub issues](https://img.shields.io/github/issues/axelniklasson/PyTrafik.svg)](https://github.com/axelniklasson/PyTrafik/issues)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

I recently had some spare time, so I decided to implement a Python wrapper to match the new release of Västtrafik's API. The goal is to provide wrappers for all endpoints in the journey planner API to make it easier to work with it.

## Getting started
### Libraries
The wrapper uses the following libraries:
* [Requests](http://docs.python-requests.org/en/latest/) to send all the API requests.
* [Tabulate](https://pypi.python.org/pypi/tabulate) to format shell output in a sweet way.

### Usage
This package is published to PyPi and can be installed using
```
pip install pytrafik
```
Documentation for this package will be added to the wiki.

### Hack on this
First make sure you have [virtualenv](https://virtualenv.readthedocs.org/en/latest/) installed.

Clone the repo
```
git clone https://github.com/axelniklasson/PyTrafik.git
```
Create virtualenv and activate it
```
cd PyTrafik
virtualenv env
source env/bin/activate
```
Install the required libraries
```
pip install -r etc/reqs.txt
```
Done!

### API credentials
The new API uses OAuth2 as authorization and in order to acquire CONSUMER_KEY and CONSUMER_SECRET from the API, one needs to subscribe to it. Please refer to [Västtrafik](https://labs.vasttrafik.se) in to get your API credentials. When they are acquired, update ```credentials.txt``` and the wrapper will work.

## Version history
* 24/11 - Version 0.1 is released!

## Contributing
Pull Requests are always welcome and should be submitted to the development branch.

### Contributors
* [persandstrom](https://github.com/persandstrom) - Support for Python 3, pip install and improved Client constructor.
* [erikkinding](https://github.com/erikkinding) - Code for livemap endpoint and all stops.
