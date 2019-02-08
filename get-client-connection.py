#!/usr/bin/env python
from __future__ import print_function
import sys
from argparse import ArgumentParser
from dnac import get_url
import json
import logging

def get_host(ip=None, mac=None):
    if ip is not None:
        url = "host?hostIp=%s" % ip
    elif mac is not None:
        url = "host?hostMac=%s" % mac
    return get_url(url)

def get_wlc(id):
    return get_url("network-device/%s" % id)

def print_host(host):
    if 'pointOfPresence' in host:
        wlc = get_wlc(host['pointOfPresence'])['response']
        connection = "-->  {hostname} {ip}  -->  {ap} vlan:{vlan}".\
            format(hostname=wlc['hostname'],
                   ip=wlc['managementIpAddress'],
                   ap=host['connectedAPName'],
                   vlan=host['vlanId'])
    else:
        connection = "-->  {name} {dev} | {interface} vlan:{vlan}".\
            format(name=host['connectedNetworkDeviceName'],
                    dev=host['connectedNetworkDeviceIpAddress'],
                   interface=host['connectedInterfaceName'],
                   vlan=host['vlanId'])

    print("{ip}|{mac} ({type}) {connection} ".
          format(ip=host['hostIp'],
                 mac=host['hostMac'],
                 type=host['hostType'],
                 connection=connection))

if __name__ == "__main__":
    parser = ArgumentParser(description='Get the connection information from a device. IP or MAC address needs to be supplied')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--ip', type=str,help="IP Address")
    parser.add_argument('-m', '--mac', type=str, help="MAC Address")
    args = parser.parse_args()

    host = get_host(args.ip, args.mac)
    print_host(host['response'][0])
