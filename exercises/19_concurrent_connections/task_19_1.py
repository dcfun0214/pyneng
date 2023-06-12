# -*- coding: utf-8 -*-
"""
Task 19.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.
Checking IP addresses should be done concurrent in different threads.

Ping_ip_addresses function parameters:
* ip_list - list of IP addresses
* limit - maximum number of parallel threads (default 3)

The function must return a tuple with two lists:
* list of available IP addresses
* list of unavailable IP addresses

You can create any additional functions to complete the task.

To check the availability of an IP address, use ping.

A hint about working with concurrent.futures:
If you need to ping several IP addresses in different threads, you need to create
a function that will ping one IP address, and then run this function in different
threads for different IP addresses using concurrent.futures (this last part
must be done in the ping_ip_addresses function).

"""
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

def ping_ip_address(ip):
    result_ping = []
    result_unping = []
    run = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE)
    run_re = re.search(r', (\d+) received,', run.stdout.decode('utf-8'))
    if int(run_re.group(1)) > 0:
        result_ping.append(ip)
    else:
        result_unping.append(ip)
    return result_ping, result_unping
def ping_ip_addresses(ip_list, limit=3):
    result_available = []
    result_unavailable = []
    final_result = (result_available, result_unavailable)
    with ThreadPoolExecutor(max_workers=limit) as excutor:
        result_ips = excutor.map(ping_ip_address, ip_list)
        for a, b in result_ips:
            if a:
                result_available.append(a[0])
            else:
                result_unavailable.append(b[0])
    return final_result


