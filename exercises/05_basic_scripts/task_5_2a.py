# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

a = input('enter the IP network in the format: 10.1.1.0/24" ')
a = a.split('/')
b = a[0].split('.')
c = "1"*int(a[1])+"0"*(32-int(a[1]))
d = (f'{int(b[0]):08b}{int(b[1]):08b}{int(b[2]):08b}{int(b[3]):08b}')
e = d[:int(a[1])] + "0"*(32-int(a[1]))
print('Network:')
print(f'{int(e[0:8], 2):<8}  {int(e[8:16], 2):<8}  {int(e[16:24], 2):<8}  {int(e[24:33], 2):<8}')
print(f'{e[0:8]:<8}  {e[8:16]:<8}  {e[16:24]:<8}  {e[24:33]:<8}')
print()
print('Mask:')
print('/'+a[1])
print(f'{int(c[0:8], 2):<8}  {int(c[8:16], 2):<8}  {int(c[16:24], 2):<8}  {int(c[24:33], 2):<8}')
print( f'{c[0:8]:8}  {c[8:16]:8}  {c[16:24]:8}  {c[24:33]:8}')

