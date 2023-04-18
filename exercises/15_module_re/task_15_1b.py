# -*- coding: utf-8 -*-
"""
Task 15.1b

Check the get_ip_from_cfg function from task 15.1a on the config_r2.txt configuration.

Note that there are two IP addresses assigned on the e0/1 interface:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

And in the dictionary returned by the get_ip_from_cfg function, only one of them
(first or second) corresponds to the Ethernet0/1 interface.

Copy the get_ip_from_cfg function from 15.1a and redesign it to return
a list of tuples for each interface in the dictionary value.
If only one address is assigned on the interface, there will be one tuple in the list.
If several IP addresses are configured on the interface, then the list will
contain several tuples. The interface name remains the key.

Check the function in the config_r2.txt configuration and make sure the
Ethernet0/1 interface matches a list of two tuples.

Please note that in this case, you can not check the correctness
of the IP address, address ranges, and so on, since the command
output from network device is processed, not user input.
"""

import re

def get_ip_from_cfg(file):
    result = {}
    with open('config_r2.txt') as f:
        for i in f.readlines():
            if i.startswith('interface'):
                a = i
                match_int = re.search(r'interface (\S+)', a)
                result[match_int.group(1)] = {}
            elif i.startswith(r' ip address') and not i.strip().endswith('secondary'):
                ip_list = []
                b = i
                match = re.search(r' ip address (\S+) (\S+)', b)
                ip_list.append(match.groups())
                result[match_int.group(1)] = ip_list
            if i.strip().endswith('secondary'):
                c = i
                match = re.search(r' ip address (\S+) (\S+) secondary', c)
                ip_list.append(match.groups())
                result[match_int.group(1)] = ip_list
    b = result.copy()
    for a in result.keys():
        if result[a] == {}:
            del b[a]
    return b
