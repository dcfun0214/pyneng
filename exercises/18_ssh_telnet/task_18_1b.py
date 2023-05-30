# -*- coding: utf-8 -*-
"""
Task 18.1b

Copy the send_show_command function from task 18.1a and rewrite it to handle
not only the exception that is raised when authentication fails on the device,
but also the exception that is raised when the IP address of the device
is not available.

When an error occurs, an exception message should be printed to standard output.

To check, change the IP address on the device or in the devices.yaml file.
"""

import yaml
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException
from netmiko import NetmikoAuthenticationException

def send_show_command(device, command):
	try:
		ssh = ConnectHandler(**device)
		output = ssh.send_command(command)
		return output
	except (NetmikoTimeoutException, NetmikoAuthenticationException) as f:
		print(f)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))


