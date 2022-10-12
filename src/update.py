import json
from pathlib import Path

# Load existing definitions
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open() as infile:
    definitions = json.load(infile)

# Update definitions manually here
definitions['animal migration'] = 'the seasonal movement of animals from one habitat to another'
definitions['paint can'] = 'a container for paint'
definitions['picture frame'] = 'a frame made to hold a picture.'
definitions['power outlet'] = 'a device to which a piece of electrical equipment can be connected in order to provide it with electricity'
definitions['see saw'] = 'a long plank balanced in the middle on a fixed support, on each end of which children sit and swing up and down by pushing the ground alternately with their feet.'
definitions['swing set'] = 'a frame for children to play on, typically including one or more swings and a slide.'
definitions['bread'] = 'food made of flour, water, and yeast mixed together and baked.'

# Store definitions in a JSON object

# Serializing json
json_object = json.dumps(definitions, indent=4)

# Writing to sample.json
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open('w') as outfile:
    outfile.write(json_object)
