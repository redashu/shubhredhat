#!/usr/bin/python2
import  time
import  platform
import  commands

options='''
Press 1 to check current  time - >>
Press 2 to open web browser - >>
Press 3 to shutdown your machine - >>
Press 4 to check current os platform - >>
Press 5 to install apache server  - >>
press 6  to  add an user jack that can only access by FTP and also configure FTP server -->>
press 7  to  change password of your root user to  newpassword  -->>
'''
print  options
# for taking input from user 
x=int(raw_input())

#print  "you have entered ",x
#  now applying  conditional statement
#  any conditional statement must follow indentation
if  x  ==  1  :
    output=time.ctime()
    print  output.split()[3]


elif   x  ==  2 :
    print  "check for browser and opening it plz wait.."
    time.sleep(1)

elif  x ==  4:
    print  "my current os platform details is :  "
    time.sleep(1)
    print  platform.version()
    time.sleep(1)
    print platform.system()

elif  x ==  5:
    print  "To install apache web server --checking os type:--"
    os_type=platform.version()
    if  'Ubuntu' in  os_type:
        print  "now install apache2 on Debain based platform.."
        print  commands.getoutput('sudo apt  install  apache2  -y')

    else :
        print  "Now installing  httpd on RPM based platform.."
        print  commands.getoutput('yum  install  httpd -y')


else  :
    print   "sorry  invalid input...>>"


 

