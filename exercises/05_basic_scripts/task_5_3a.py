# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

config_template = {
    'access': access_template,
    'trunk': trunk_template,
    }

question = {
	'access': 'Enter VLAN number: ',
	'trunk': 'Enter the allowed VLANs: ',
	}

port_mode = input('Enter interface mode (access/trunk): ')
interface_num = input('Enter interface type and number: ')
vlan_num = input(question[port_mode])
print(f'interface {interface_num}')
print('\n'.join(config_template[port_mode]).format(vlan_num))

