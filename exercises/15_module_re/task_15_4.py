# -*- coding: utf-8 -*-
"""
Task 15.4

Create a get_ints_without_description function that expects as an argument
the name of the file containing the device configuration.

The function should process the configuration and return a list of interface names,
which do not have a description (description command).

An example of a final list:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

An example of an interface with a description:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Interface without description:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Check the operation of the function using the example of the config_r1.txt file.
"""

import re

def get_ints_without_description(file):
    with open('config_r1.txt') as fs:
        match_all = []
        for i in fs.readlines():
            if i.startswith('interface'):
                a = re.search(r'interface (\S+)', i)
                match_all.append(a.group(1))
            elif i.startswith(' description'):
                match_all.remove(a.group(1))
    return match_all
