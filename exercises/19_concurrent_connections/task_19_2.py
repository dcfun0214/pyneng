# -*- coding: utf-8 -*-
"""
Task 19.2

Create a send_show_command_to_devices function that sends the same show command
to different devices in concurrent threads and then writes the output of
the commands to a file. The output from the devices in the file can be in any order.

Function parameters:
* devices - a list of dictionaries with parameters for connecting to devices
* command - show command
* filename - is the name of a text file to which the output of all commands will be written
* limit - maximum number of concurrent threads (default 3)

The function returns None.

The output of the commands should be written to a plain text file in this
format (before the output of the command, you must write the hostname and
the command itself):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

You can create any additional functions to complete the task.

Check the operation of the function on devices from the devices.yaml file.
"""
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import yaml

with open('devices.yaml') as f:
	dev = yaml.safe_load(f)

def send_show_command_to_device(device, command):
    a = f'{device["host"]}'
    with ConnectHandler(**device, session_log=a) as con:
        con.enable()
        output = con.send_command(command)
    with open(a) as f:
        a=f.readlines()
        for i in a:
            if command in i:
                start = a.index(i)
            if 'exit' in i:
                end = a.index(i)
        b = a[int(start):end-1]
        x = ''.join(b)
    return x.strip()

def send_show_command_to_devices(devices, command, filename, limit):
    result = []
    with ThreadPoolExecutor(max_workers=limit) as excutor:
        run = excutor.map(send_show_command_to_device, devices, repeat(command))
        for i in run:
            result.append(i)
    write_down = '\n'.join(result)
    with open(filename, 'w') as f:
        f.write(write_down)
