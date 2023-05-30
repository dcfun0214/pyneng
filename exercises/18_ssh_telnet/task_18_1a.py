# -*- coding: utf-8 -*-
"""
Task 18.1a

Copy the send_show_command function from task 18.1 and rewrite it to handle
the exception that is thrown on authentication failure on the device.

When an error occurs, an exception message should be printed to stdout.

To verify, change the password on the device or in the devices.yaml file.

"""


import yaml
from netmiko import ConnectHandler


def send_show_command(device, command):
	try:
		ssh = ConnectHandler(**device)
		output = ssh.send_command(command)
		return output
	except:
		print('authentication')


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))

