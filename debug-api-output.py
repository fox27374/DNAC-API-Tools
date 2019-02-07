#!/usr/bin/env python
from __future__ import print_function
import sys
import json
from argparse import ArgumentParser
from dnac import get_url

if __name__ == "__main__":
    parser = ArgumentParser(description='Prints the API response in a formated way')
    parser.add_argument('-u', '--url', type=str, help="URL",required=True)
    args = parser.parse_args()
    
    # Get device list
    response = get_url(args.url)
    
    # Check if filters are applied
    print(json.dumps(response, indent=4, sort_keys=True))
