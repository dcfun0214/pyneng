# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
with open('CAM_table.txt', 'r') as f:
#     print(f.readlines())
    for i in f.readlines():
        list1.append(i.strip())
for i in list1:
    if i == '':
        list1.remove(i)
    elif i.split()[0][-1] == '0':
        list2.append(i)
for x in list2:
    y = x.replace('DYNAMIC', '')
    list3.append(y)
for a in list3:
    list4.append(a.split())
for i in list4:
    i[0] = int(i[0])
list4.sort()
# print(list4)


ask_vlan = input('Enter VLAN number: ')
for i in list4:
    if i[0] == int(ask_vlan):
        list5.append(i)
for a, b, c  in list5:
    print(f"{a:<9}{b:20}{c}")


