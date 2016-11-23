#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from client import Client
from tabulate import tabulate

client = Client(format='JSON')

print('\n### API Wrapper DEMO ###')

vehiclePositions = client.get_livemap(12.246026, 57.831061, 11.544078, 57.533878)
print('\n### Current vehicle positions')
table = []
for pos in vehiclePositions:
	row = []
	row.append(pos['name'])
	row.append(pos['y'])
	row.append(pos['x'])

	delay = 0
	if 'delay' in pos.keys():
		delay = pos['delay']
	row.append(delay)
	table.append(row)

headers = ['Name', 'Lat', 'Lon', 'Delay (minutes)']
print(tabulate(table, headers=headers))

stops = client.get_stops_by_name('Domkyrkan')
print('\n### Search results for "Domkyrkan" ###')
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
