#!/usr/bin/python2

import  sys
import  commands
software_name=sys.argv[1:]

for  i  in  software_name:
    print  commands.getoutput('yum   install   -y   '+i)
