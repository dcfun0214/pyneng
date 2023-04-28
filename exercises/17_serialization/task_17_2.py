# -*- coding: utf-8 -*-
"""
Task 17.2

In this task you need:
* take the contents of several files with the output of the sh version command
* parse command output using regular expressions and get device information
* write this information to a file in CSV format

To complete the task, you need to create two functions.

parse_sh_version function:
* expects the output of the sh version command as an argument in single string (not a filename)
* processes output using regular expressions
* returns a tuple of three elements:
 * ios - "12.4(5)T"
 * image - "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - "5 days, 3 hours, 3 minutes"

The write_inventory_to_csv function must have two parameters:
* data_filenames - expects a list of filenames as an argument with
  the output of sh version
* csv_filename - expects as an argument the name of a file (for example,
  routers_inventory.csv) to which information will be written in CSV format

write_inventory_to_csv function writes the contents to a file, in CSV format and returns nothing.

The write_inventory_to_csv function should do the following:
* process information from each file with sh version output:
  sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* using the parse_sh_version function, ios, image, uptime information
  should be obtained from each output
* from the file name you need to get the hostname
* after that all information should be written to a CSV file

The routers_inventory.csv file should have the following columns (in this order):
* hostname, ios, image, uptime

The code below has created a list of files using the glob module.
You can uncomment the print(sh_version_files) line to see the content of the list.

In addition, a list of headers has been created, which should be written to CSV.
"""

import glob
import re
import csv

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)
headers = ["hostname", "ios", "image", "uptime"]

def write_inventory_to_csv(data_filenames, csv_filename):
    result_csv = []
    for i in data_filenames:
        with open(i) as f:
            a = list(parse_sh_version(f.read()))
            a.insert(0, f.name[-6:-4])
            result_csv.append(a)
    result_csv.insert(0, headers)
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result_csv)


def parse_sh_version(output):
    re_search = re.search(r'Cisco IOS Software.*Version (\S+),.*Technical Support.*router uptime is (\d+ days, \d+ hours, \d+ minutes).*System image file is "(\S+)"', output, re.DOTALL )
    result_sub = re_search.group(1, 3, 2)
    return result_sub

