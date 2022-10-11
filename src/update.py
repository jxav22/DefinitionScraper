import json
from pathlib import Path

# Load existing definitions
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open() as infile:
    definitions = json.load(infile)

# Update definitions manually here
definitions['animal migration'] = ''
definitions['paint can'] = ''
definitions['picture frame'] = ''
definitions['power outlet'] = ''
definitions['see saw'] = ''
definitions['swing set'] = ''

# Store definitions in a JSON object

# Serializing json
json_object = json.dumps(definitions, indent=4)

# Writing to sample.json
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open('w') as outfile:
    outfile.write(json_object)