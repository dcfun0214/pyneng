# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""


a = input('enter the IP network in the format: 10.1.1.0/24" ')
a = a.split('/')
b = a[0].split('.')
c = "1"*int(a[1])+"0"*(32-int(a[1]))
print('Network:')
print(f'{b[0]:8}  {b[1]:8}  {b[2]:8}  {b[3]:8}')
print( f'{int(b[0]):08b}  {int(b[1]):08b}  {int(b[2]):08b}  {int(b[3]):08b}' )
print()
print('Mask:')
print('/'+a[1])
print(f'{int(c[0:8], 2):<8}  {int(c[8:16], 2):<8}  {int(c[16:24], 2):<8}  {int(c[24:33], 2):<8}')
print( f'{c[0:8]:8}  {c[8:16]:8}  {c[16:24]:8}  {c[24:33]:8}')
