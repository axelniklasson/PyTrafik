#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from client import Client
from tabulate import tabulate

##
def demo_vehicle_positions(client):
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

def demo_get_stops_by_name(client):
	stops = client.get_stops_by_name(stop_name)
	print('\n### Search results for "'+stop_name+'" ###')
	for stop in stops:
		print(stop['name'])

def demo_get_arrivals(client):
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

def demo_get_departures(client):
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

# This method should be used only when needed
# It's a heavy request, and stops don't change very often
def demo_get_all_stops(client):
	print('\n### List all stops ###')
	
	stops = client.get_all_stops()
	table = []

	for stop in stops:
		row = []
		row.append(stop['name'])
		
		track = ''
		if('track' in stop.keys()):
			track = stop['track']
		
		row.append(track)
		row.append(stop['lat'])
		row.append(stop['lon'])
		table.append(row)

	headers = ['Name', 'Track', 'Lat', 'Lon']
	print(tabulate(table, headers=headers))
	print('\n')

##

# Domkyrkan
stop_name = 'Domkyrkan'
# stop_id for Domkyrkan
stop_id = '9021014002130000'

client = Client(format='JSON')

print('\n### API Wrapper DEMO ###')
#demo_get_all_stops(client)
#demo_vehicle_positions(client)
#demo_get_departures(client)
demo_get_arrivals(client)
#demo_get_stops_by_name(client)