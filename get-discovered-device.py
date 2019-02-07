#!/usr/bin/env python
from __future__ import print_function
import sys
import json
from argparse import ArgumentParser
from dnac import get_url

def create_filtered_list(response):
    f_list=[]
    for device in response["response"]:
        if args.ip and args.ip in device['hostIp']:
            f_list.append(device)
        if args.mac and args.mac in device['hostMac']:
            f_list.append(device)
        if args.type and args.type in device['hostType']:
            f_list.append(device)
        if args.ssid and 'wireless' in device['hostType'] and args.ssid in device['wlanNetworkName']:
            f_list.append(device)
    return f_list

if __name__ == "__main__":
    parser = ArgumentParser(description='Filter results based on the device attributes containing the supplied string. Multiple filters behave in an OR manner.')
    parser.add_argument('-i', '--ip', type=str, help="IP Address")
    parser.add_argument('-m', '--mac', type=str, help="MAC Address")
    parser.add_argument('-t', '--type', type=str, help="Type")
    parser.add_argument('-s', '--ssid', type=str, help="SSID")
    args = parser.parse_args()
    
    # Get device list
    response = get_url('host')
    
    # Print header
    print("{0:25}{1:18}{2:20}{3:12}{4:18}".format("Device", "IP Address", "MAC Address", "Type", "SSID"))

    # Check if filters are applied
    if len(sys.argv) <= 1:
        filtered_list = response["response"]
    else:
        filtered_list = create_filtered_list(response)

    for device in filtered_list:
        #print(device['hostIp'])
        if 'wireless' in device['hostType']:
            ssid = device['wlanNetworkName']
            device_type = device["hostDeviceType"]
        else:
            ssid = 'N/A'
            device_type = 'Unknown'
        print("{0:25}{1:18}{2:20}{3:12}{4:18}".format(device_type, device['hostIp'], device['hostMac'], device['hostType'], ssid))
