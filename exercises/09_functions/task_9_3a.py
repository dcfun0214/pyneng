# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

def get_int_vlan_map(config_filename):
	access_port = {}
	trunk_port = {}
	result = [access_port, trunk_port]
	with open(config_filename) as f:
		for a in f.readlines():
			if a.startswith('interface'):
				inf = a.split()[-1]
			elif a.strip() == 'switchport mode access':
				access_port[inf] = 1
			elif 'access vlan' in a:
				access_port[inf] = int(a.split()[-1])
			elif 'allowed vlan' in a:
				trunk_port[inf] = [int(v) for v in a.split()[-1].split(",")]
	return tuple(result)

