"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot as a map.

Part III: Take the data we parsed earlier and create a different format
for rendering a map. Here, we parse through each line item of the
CSV file and create a geojson object, to be collected into one geojson
file for uploading to gist.github.com.
"""

import geojson 

import parse as p

def create_map(data_file):
	"""Creates a GeoJSON file.

	Returns a GeoJSON file that can be rendered in a GitHub
	Gist at gist.github.com. Just copy the output file and 
	paste into a new Gist, then create either a public or
	private gist. GitHub will automatically render the GeoJSON
	file as a map.
	"""
	# define type of GeoJSON we're creating
	geo_map = {"type": "FeatureCollection"}

	# define empty list to collect each point to graphs
	item_list = []

	# iterate over data to create GeoJSON document
	# use enumerate() to get line AND index
	for index, line in enumerate(data_file):

		# skip any zero coordinates
		if line['X'] == "0" or line['Y'] == "0":
			continue

		# set up new dict for each iteration
		data = {}

		# assign line items to appropriate GeoJSON fields
		data['type'] = 'Feature'
		data['id'] = index
		data['properties'] = {'title': line['Category'],
							  'description': line['Descript'],
							  'date' : line['Date']}
		data['geometry'] = {'type': 'Point',
						    'coordinates': (line['X'], line['Y'])}

		# add data dict to item_list
		item_list.append(data)

	# for each point in item_list, add point to dict
	# setdefault creates "features" key that has valye type of empty list
	# we append point to list with each iteration

	for point in item_list:
		geo_map.setdefault('features', []).append(point)

	# write parsed GeoJSON data to file to upload to gist
	with open('file_sf.geojson', 'w') as f:
		f.write(geojson.dumps(geo_map))

def main():
	# Call parse function, give it proper parameters
	new_data = p.parse(p.MY_FILE, ",")

	return create_map(new_data)


if __name__ == "__main__":
	main()
