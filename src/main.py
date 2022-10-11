import csv
from pathlib import Path

# Load words from the csv file
file_location = '../resources/category_difficulty.csv'
path = Path(__file__).parent / file_location

words = []

with path.open() as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        words.append(row[0])

# Scrape definitions

# Store definitions in a JSON object
