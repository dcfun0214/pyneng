# -*- coding: utf-8 -*-
"""
Task 11.2

Create a create_network_map function that processes the show cdp neighbors
command output from multiple files and merges it into one common topology.

The function must have one parameter, filenames, which expects as an argument
a list of filenames containing the output of the show cdp neighbors command.

The function should return a dictionary that describes the connections
between devices. The structure of the dictionary is the same as in task 11.1:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}


Generate topology that matches the output from the files:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Do not copy the code of the parse_cdp_neighbors and draw_topology functions.
If the parse_cdp_neighbors function cannot process the output of one of the
command output files, you need to correct the function code in task 11.1.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
from task_11_1 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    jieguo={}
    result_all = []
    q = []
    e = []
    for file in filenames:
        with open(file) as f:
            result_all.append(parse_cdp_neighbors(f.read()))
    for i in result_all:
        for x, y in i.items():
            q.append(x)
            e.append(y)
    jieguo=dict(zip(q,e))
    return jieguo
