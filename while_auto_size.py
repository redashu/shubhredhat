#!/usr/bin/python2

import  commands
import time



#check_size=commands.getoutput('df -h /   |  tail -1 ')
#print check_size.split()[3]
while 2 > 1 :
    check_size=commands.getoutput('df -h /   |  tail -1 ')
    val=check_size.split()[3]

    if  val  == '12G' :
        print "extending  lvm "
        print  commands.getoutput('echo  extended')
        time.sleep(5)
    else :
        print  "we have enough size as of now..."
        time.sleep(10)

