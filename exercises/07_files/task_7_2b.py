# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv
src_file = argv[1]
dst_file = argv[2]
lines = []
with open(src_file, 'r') as src:
    for line in src:
        lines.append(line)
        for b in ignore:
            for i in lines:
                if i.startswith('!'):
                    lines.remove(i)
                elif b in i:
                    lines.remove(i)

with open(dst_file, 'w') as dst:
	dst.write(''.join(lines))
