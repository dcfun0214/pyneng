# -*- coding: utf-8 -*-
"""
Task 19.3a

Create a send_command_to_devices function that sends a list of the specified
show commands to different devices in concurrent threads, and then writes the
output of the commands to a file. The output from the devices in the file can
be in any order.

Function parameters:
* devices - a list of dictionaries with parameters for connecting to devices
* commands_dict - a dictionary that specifies which device to send which commands.
  Dictionary example - commands
* filename is the name of the file to which the output of all commands will be written
* limit - maximum number of parallel threads (default 3)

The function returns None.

The output of the commands should be written to a plain text file in this
format (before the output of the command, you must write the hostname and
the command itself):

R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R1#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
R3#sh ip route | ex -

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0

To complete the task, you can create any additional functions,
as well as use the functions created in previous tasks.

Check the operation of the function on devices from the devices.yaml file
and the commands dictionary
"""

# This dictionary is only needed to check the operation of the code;
# you can change the IP addresses in it.
# The test takes addresses from the devices.yaml file
commands = {
    "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
    "192.168.100.1": ["sh ip int br", "sh int desc"],
    "192.168.100.2": ["sh int desc"],
}

from task_19_2 import send_show_command_to_device
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_command_to_devices(devices, commands_dict, filename, limit):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		write_down = []
		result = []
		for dev in devices:
			for comm in commands_dict[dev['host']]:
				run = executor.submit(send_show_command_to_device, dev, comm)
				write_down.append(run)
		for i in as_completed(write_down):
			result.append(i.result())
			b = '\n'.join(result)
	with open(filename, 'w') as f:
		f.write(b)





