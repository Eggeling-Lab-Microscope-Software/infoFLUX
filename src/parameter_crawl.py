## Dependencies
import os, sys
from typing import NoReturn
import json
sys.path.insert(0, '../')

from pyDialogue import askFILE

def parameter_crawl()->NoReturn:
    """
    This function is used to crawl through the data field parameters of a MINFLUX json file.
    
    """
    ## load data
    file = askFILE() # grab filepath using windows dialog
    if file.endswith('.json'):
        with open(file, 'r') as f:
            data = json.load(f)
    else:
        raise ValueError('File must be a json file')

    ## As the data is dumped during each iteration consistently, 
    # we need to only look at one iteration to get all keys
    data = data[0]

    # let's look at the keys
    external_keys = set(list(data.keys()))
    internal_keys = []

    for item in data['itr']:
        internal_keys.append(list(item.keys()))
        
    from itertools import chain
    external_keys = sorted(external_keys)
    internal_keys = sorted(set(list(chain.from_iterable(internal_keys))))

    external_values = {key:data[key] for key in external_keys if key != 'itr'}
    internal_values = {key:[item[key] for item in data['itr']] for key in internal_keys if key != 'mode'}

    print('external keys: ', external_keys)
    print('internal keys: ', internal_keys)
    ## print values
    from pprint import pformat
    print('external values: ', pformat(external_values))
    print('internal values: ', pformat(internal_values))
    
if __name__ == "__main__":
    parameter_crawl()