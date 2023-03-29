# -*- coding: utf-8 -*-
"""
Task 9.1a

Make a copy of the code from the task 9.1.

Add this functionality: add an additional parameter that controls whether
port-security configured
  * parameter name 'psecurity'
  * default is None
  * to configure port-security, a list of commands must be passed as a value
    port-security (port_security_template list)

The function should return a list of all ports in access mode with configuration
based on the access_mode_template template and the port_security_template template,
if passed. There should not be a new line character at the end of lines in the list.

Check the operation of the function using the example of the access_config
dictionary, with the generation of the configuration port-security and without.

An example of a function call:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    """
    intf_vlan_mapping is a dictionary with interface-VLAN mapping:
         {'FastEthernet0/12': 10,
          'FastEthernet0/14': 11,
          'FastEthernet0/16': 17}
    access_template - list of commands for the port in access mode

    Returns a list of commands.
    """
    result = []
    for a, b in intf_vlan_mapping.items():
        result.append(f'interface {a}')
        for c in access_template:
            if c.endswith('vlan'):
                result.append(f'{c} {b}')
            else:
                result.append(c)
        if psecurity:
            for d in port_security_template:
                result.append(d)
    return result
