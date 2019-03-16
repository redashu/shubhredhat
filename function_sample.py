#!/usr/bin/python2

import time,commands,os

#  creating  function  
def  mesg():

    print  "Hey shubhdha...how are u ....?"
    print  "hopefully doing great..this weekend.."
    print  "good work at redhat.."

def    resource_check():
        print commands.getoutput('free -m')
        time.sleep(2)
        print commands.getoutput('lscpu')


############### defining  new task ######### 

options='''
press  1  to check  all free resources (RAM &  CPU ) : 
press  2  to get currnet time  :
press  3  to chat with project lead ..
'''
print  options
x=raw_input()

if  x  ==  '1':
    resource_check()

else  :
    print  "invalid input"
