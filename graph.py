"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt 
import numpy as np 

from parse import parse

MY_FILE = "../dataviz/data/sample_sfpd_incident_all.csv"

def visualize_days(data):
	"""Visualize data by day of week"""

	# grab parsed data from earlier
	#data_file = parse(MY_FILE, ",")

	# make a new variable 'counter', 
	# from iterating through each line of data
	# and count how many incidents happen on each day of the week

	counter = Counter(item["DayOfWeek"] for item in data)

	## TO DO challenge: rewrite for loop for counter

	# separate x-axis data (day of week)
	# from 'counter' variable from y-axis 
	# (# incidents in a day)

	data_list = [
				 counter["Monday"],
				 counter["Tuesday"],
				 counter["Wednesday"],
				 counter["Thursday"],
				 counter["Friday"],
				 counter["Saturday"],
				 counter["Sunday"]
				]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	# assign y-axis data to matplotlib plot instance
	plt.plot(data_list)

	# create necessary number of ticks for x-axis, assign labels
	plt.xticks(range(len(day_tuple)), day_tuple)

	# save plot
	plt.savefig("Days.png")

	# close plot file
	plt.clf()

def visualize_type(data):
	# make counter by category
	counter = Counter(item["Category"] for item in data)

	# set labels, order doesn't matter so use counter.keys()
	labels = tuple(counter.keys())

	# set where labels hit x-axis
	xlocations = np.arange(len(labels)) + 0.5

	# set width of bars plotted
	width = 0.5

	# assign data to bar plot
	plt.bar(xlocations, counter.values(), width = width)

	# assign labls and tick locations to x-axis
	plt.xticks(xlocations + width / 2, labels, rotation = 90)

	# add room so not cutting of x labels
	plt.subplots_adjust(bottom = 0.4)

	# make graph bigger
	plt.rcParams['figure.figsize'] = 12, 8

	# save graph
	plt.savefig("Type.png")

	# close plot figure
	plt.clf

def main():
	# Call parse function, give it proper parameters
	new_data = parse(MY_FILE, ",")

	# Make graph of day distribution
	visualize_days(new_data)

	# Make graph of type distribution
	visualize_type(new_data)


if __name__ == "__main__":
	main()
