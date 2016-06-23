#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from client import Client
from tabulate import tabulate

client = Client(format='JSON')

print('\n### API Wrapper DEMO ###')

stops = client.get_stops_by_name('Brunnsparken')
print('\n### Search results for "Brunnsparken" ###')
for stop in stops:
	print(stop['name'])
stop = stops[0]
stop_id = stop['id']
stop_name = stop['name']

arrivals = client.get_arrivals(stop_id)
print('\n### Arrivals at ' + stop_name + ' ###')
table = []
for arr in arrivals:
	row = []
	row.append(arr['name'])
	row.append(arr['origin'])
	row.append(arr['time'])
	row.append(arr['track'])
	table.append(row)

headers = ['Name', 'Origin', 'Time', 'Track']
print(tabulate(table, headers=headers))
print('\n')

departures = client.get_departures(stop_id)
print('\n### Departures from ' + stop_name + ' ###')
table = []
for dep in departures:
	row = []
	row.append(dep['name'])
	row.append(dep['direction'])
	row.append(dep['time'])
	row.append(dep['track'])
	table.append(row)

headers = ['Name', 'Destination', 'Time', 'Track']
print(tabulate(table, headers=headers))
print('\n')
