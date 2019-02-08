# DNAC-API-Tools

This repository contains different python scripts to interact with the Cisco DNA Center through the APIs. Base and inspiration for the scripts came from CiscoDevNet.
All the scripts were tested and developed using the DNAC version 1.2.8

## Config file
Please modify the file dnac_config.py and adapt it to you needs.

## get-device-list.py
This script will show all of the network devices in the inventory of Cisco DNA Center. Filters can be applied via arguments.
```buildoutcfg
./get-device-list.py
./get-device-list.py --ip 10.10.22.70
./get-device-list.py --hostname cisco

```

## get-device-interface.py
This script will show you all the switch interfaces and some information with them. Currently only for switches. IP needs to be supplied.
```buildoutcfg
./get-device-interface.py --ip 172.24.89.254

```

## get-client-list.py
This script will show all of the network clients discovered and connected to one of the network devices in the DNAC. Filters can be applied via arguments.
```buildoutcfg
./get-client-list.py
./get-client-list.py --ip 10.10.22.70

```

## get-client-connection.py
This script will show you where the client is connected to (e.g. switch interface and vlan). IP or MAC needs to be supplied.
```buildoutcfg
./get-client-connection.py --ip 172.24.80.144

```

## debug-api-output.py
This script just prints the API responde in a formated way.
```buildoutcfg
./debug-api-output.py -u host

```
