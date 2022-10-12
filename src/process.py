import json
import re
from pathlib import Path
from wiktionaryparser import WiktionaryParser

# Load existing definitions
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open() as infile:
    definitions = json.load(infile)

# Update definitions manually here
parser = WiktionaryParser()


def get_definition(word):
    parsed_word = parser.fetch(word)
    word_definitions = parsed_word[0].get('definitions')
    if not word_definitions:
        return None
    else:
        return word_definitions[0].get('text')[1]


def remove_first_brackets(text):
    return re.sub(r'^\(.+\)\s', '', text)


def remove_plurals(text):
    match = re.search(r'plural of (\w+)', text)
    if not match:
        return text
    else:
        text = get_definition(match.group(0))
        return text


for key, value in definitions.items():
    definitions[key] = remove_plurals(value)

# Store definitions in a JSON object

# Serializing json
json_object = json.dumps(definitions, indent=4)

# Writing to sample.json
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open('w') as outfile:
    outfile.write(json_object)
