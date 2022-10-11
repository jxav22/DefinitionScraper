import csv
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

# Scrape definitions
parser = WiktionaryParser()


def get_definition(word):
    parsed_word = parser.fetch(word)
    definitions = parsed_word[0].get('definitions')
    if not definitions:
        return None
    else:
        return definitions[0].get('text')[1]


for i in range(10):
    definition = get_definition(words[i])
    if not definition:
        print(f'{words[i]} DID NOT RETURN A VALUE')
    else:
        print(f'{words[i]}: {definition}')

# Store definitions in a JSON object
