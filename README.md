# DNAC-API-Tools

This repository contains different python scripts to interact with the Cisco DNA Center through the APIs
Base and inspiration for the scripts came from CiscoDevNet.

## Config file
Please modify the file dnac_config.py and adapt it to you needs.

## get-network-device.py
This script will show all of the network devices in the inventory of Cisco DNA Center. Filters can be applied via arguments.
```buildoutcfg
./get-network-device.py
./get-network-device.py --ip 10.10.22.70
./get-network-device.py --hostname cisco

```
