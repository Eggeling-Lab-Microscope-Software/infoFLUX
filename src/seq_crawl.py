## Dependencies
import os, sys
import json
sys.path.insert(0, '../')

from pyDialogue import askFILE

## load data
file = askFILE() # grab filepath using windows dialog
with open(file, 'r') as f:
    data = json.load(f)
    
# let's look at the keys
external_keys = set(list(data.keys()))
internal_keys = []

for item in data['Itr']:
    internal_keys.append(list(item.keys()))
    
from itertools import chain
external_keys = sorted(external_keys)
internal_keys = sorted(set(list(chain.from_iterable(internal_keys))))
innermost_keys = sorted(set(list(chain.from_iterable([list(item['Mode'].keys()) for item in data['Itr']]))))

external_values = {key:data[key] for key in external_keys if key != 'Itr'}
internal_values = {key:[item[key] for item in data['Itr']] for key in internal_keys if key != 'Mode'}
innermost_values = {key:[item[key] for item in [outer['Mode'] for outer in data['Itr']]] for key in innermost_keys}

print('external keys: ', external_keys)
print('internal keys: ', internal_keys)
print('innermost keys: ', innermost_keys)

## print values
from pprint import pformat
print('external values: ', pformat(external_values))
print('internal values: ', pformat(internal_values))
print('innermost values: ', pformat(innermost_values))