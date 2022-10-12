import csv
import json
import re
from pathlib import Path
from wiktionaryparser import WiktionaryParser

# Load words from the csv file
file_location = '../resources/category_difficulty.csv'
path = Path(__file__).parent / file_location

words = []

with path.open() as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        words.append(row[0])

# Load existing definitions
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open() as infile:
    definitions = json.load(infile)

# Scrape definitions
parser = WiktionaryParser()


def get_definition(word):
    parsed_word = parser.fetch(word)
    word_definitions = parsed_word[0].get('definitions')
    if not word_definitions:
        return None
    else:
        return word_definitions[0].get('text')[1]


def preprocess_word(word):
    if word.startswith('The '):
        word = word[4:]
        return word
    else:
        return word


for i in range(1):
    word = words[i]
    print(word)

    definition = get_definition(preprocess_word(word))
    if not definition:
        print(f'{word} DID NOT RETURN A VALUE')
    else:
        definitions[word] = definition

print(definitions)
# Store definitions in a JSON object

# Serializing json
json_object = json.dumps(definitions, indent=4)

# Writing to sample.json
file_location = '../resources/definitions.json'
path = Path(__file__).parent / file_location

with path.open('w') as outfile:
    outfile.write(json_object)
