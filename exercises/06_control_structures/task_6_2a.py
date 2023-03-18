# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
IP = input('enter an IP address in the format 10.0.1.1: ')
correct_ip = []
IP_List = IP.split('.')
if len(IP_List) == 4:
    for i in IP_List:
        try:
            if int(i) < 0 or int(i) > 255:
                print('Invalid IP address')
                break
            elif IP.count('.') != 3:
                print('Invalid IP address')
                break
        except:
            print('Invalid IP address')
            break
    else:
        correct_ip = IP_List
        if  1 < int(correct_ip[0]) < 223:
            print('unicast')
        elif 224 < int(correct_ip[0]) < 239:
            print('multicast')
        elif '.'.join(correct_ip) == '255.255.255.255':
            print('local broadcast')
        elif '.'.join(correct_ip) == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
else:
    print('Invalid IP address')


