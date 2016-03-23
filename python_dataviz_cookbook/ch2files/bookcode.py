#__AUTHOR: Di

import csv
filename = 'ch02-data.csv'
data = []

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    print "Error reading CSV file at line %s: %s" % (reader.line_num, e)
    sys.exit(-1)
    # The exit code is an 8-bit value on Unix
    # exit(0) means a clean exit without any errors / problems
    # exit(1) means there was some issue / error / problem and that is why the program is exiting.
    # If you invoke exit(-1), the value is equivalent to exit(255)

if header:
    print header
    print '============='

for datarow in data:
    print datarow


# jSON

import requests
from pprint import pprint

url = 'https://api.github.com/users/justglowing'
r = requests.get(url)
json_obj = r.json()
pprint(json_obj)

import json
jstring = '{"name" : "prod1", "price" : 12.50}'
from decimal import Decimal
json.loads(jstring, parse_float=Decimal)




