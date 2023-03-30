# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv
file = argv[1]
#lines = []
#with open(file, 'r') as f:
#    for line in f:
#        lines.append(line)
#        for b in ignore:
#            for i in lines:
#                if i.startswith('!'):
#                    lines.remove(i)
#                elif b in i:
#                    lines.remove(i)
#
#print(''.join(lines))

with open(file, 'r') as f:
    x = f.readlines()
    for a in ignore:
        for b in x:
            if b.startswith('!') or a in b:
                x.remove(b)
    for i in x:
        print(i.rstrip())

