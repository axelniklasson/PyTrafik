#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client import Client
from tabulate import tabulate

client = Client()

stops = client.search_stops('Brunnsparken')
# Brunnsparken, Göteborgs is first in response
stop = stops[0]
stopID = stop['id']

departures = client.get_departures(stopID)

print '\n### Departures at ' + stop['name'] + ' ###'
table = []
for dep in departures:
	row = []
	row.append(dep['name'])
	row.append(dep['direction'])
	row.append(dep['time'])
	row.append(dep['track'])
	table.append(row)

headers = ['Name', 'Direction', 'Time', 'Track']
print tabulate(table, headers=headers)
print '\n'