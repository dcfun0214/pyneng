from sys import argv

interface = argv[1]
vlan = argv[2]

access_template = [
'sw mo acc',
'sw acc v {}',
'sw  nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable'
]

print('interface{}'.format(interface))
print('\n'.join(access_template).format(vlan))
