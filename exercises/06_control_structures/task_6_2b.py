# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

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
		IP = input('enter an IP address in the format 10.0.1.1: ')
                break
            elif IP.count('.') != 3:
                print('Invalid IP address')
		IP = input('enter an IP address in the format 10.0.1.1: ')
                break
	except:
            print('Invalid IP address')
            IP = input('enter an IP address in the format 10.0.1.1: ')
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
    IP = input('enter an IP address in the format 10.0.1.1: ')

