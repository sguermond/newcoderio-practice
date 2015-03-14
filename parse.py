"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv

MY_FILE = "../dataviz/data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-line object."""
	### tutorial comment: need to fix code display
	# Open CSV file
	opened_file = open(raw_file)

	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter = delimiter)
	
	# Set up empty list
	parsed_data = []

	# Get header from first line of code
	fields = csv_data.next() ### tutorial comment: should this say it is an iterator?

	# iterate over each row of file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close CSV file
	opened_file.close()

	# Build a data structure to return parsed data
	return parsed_data


def main():
	# Call parse function, give it proper parameters
	new_data = parse(MY_FILE, ",")

	# Let's see what the data looks like!
	print new_data


if __name__ == "__main__":
	main()
