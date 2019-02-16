#!/usr/bin/python2

import  sys

numbers=sys.argv[1:]
print numbers

sum=0
for  i   in  numbers :
    sum=sum+int(i)

print  sum

'''
n1=raw_input("enter  number  1 :  ")
n2=raw_input("enter  number  2 :  ")
print  int(n1) +  int(n2)
'''
