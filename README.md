# Västtrafik API wrapper
I recently had some spare time, so I decided to implement a Python wrapper to match the new release of Västtrafik's API. The goal is to provide wrappers for all endpoints in the journey planner API to make it easier to work with it.

## Getting started
### Libraries
The wrapper uses the following libraries:

[Requests](http://docs.python-requests.org/en/latest/) to send all the API requests

[Tabulate](https://pypi.python.org/pypi/tabulate) to format shell output in a sweet way

### Setup
First make sure you have [virtualenv](https://virtualenv.readthedocs.org/en/latest/) installed.

Clone the repo
```
git clone https://github.com/axelniklasson/vasttrafik-api-wrapper.git
```
Create virtualenv and activate it
```
cd vasttrafik-api-wrapper
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

## Contributors
* [persandstrom](https://github.com/persandstrom) - Support for Python 3.
* [erikkinding](https://github.com/erikkinding) - Code for livemap endpoint.
