# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
#output_template = '''
#{:20}{:20}
#{:20}{:20}
#{:20}{:20}
#{:20}{:20}
#{:20}{:20}
#'''

#with open('ospf.txt', 'r') as f:
#    for line in f:
#        i = line.split()
#        print(output_template.format('Prefix', i[1].replace(',',''),'AD/Metric',i[2].replace(']','').replace('[',''),'Next-Hop',i[4].replace(',',''),'Last update',i[5].replace(',',''),'Outbound Interface',i[6]))

output_template = '''
{:25}{}
{:25}{}
{:25}{}
{:25}{}
{:25}{}
'''
with open('ospf.txt', 'r') as f:
    for line in f:
        lines = line.replace('[','').replace(']','').replace(',','')
        print(output_template.format('Prefix',lines.split()[1],
              'AD/Metric',lines.split()[2],
              'Next-Hop',lines.split()[4],
              'Last update',lines.split()[5],
              'Outbound Interface',lines.split()[6],
              ))



