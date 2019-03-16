#!/usr/bin/python2

import  time
#  creating an empty  file  
#     file name ,   file mode ==(r,w,a)
f=open('/tmp/myfile1.txt','w')
print  "file is created.."
f.close()


#  create  file and write some data

f=open('/tmp/shubhdha.txt','w')
#print  "file is created..."
#print   "writing  some random data .."
time.sleep(2)
f.write("hey guys")
f.close()


#  writing  another  data  
'''
remember  write mode always override previous data
in write mode you can not read the file content 
'''

f=open('/tmp/shubhdha.txt','w')
f.write("hello world this is me ")
f.write("\n")
f.write("adding more data")
f.close()

# now opening a file for read only
f=open('/etc/hosts','r')
data=f.read()
print data
f.close()

#  now read and write both in  a new file 
f=open('/tmp/shubhdha1.txt','w+')
f.write("wrrrisdfldsf")
f.write('\n')
#  to change cursor position
f.seek(0)
x=f.read()
print x
f.close()

#  there is another mode called   r+ --- same as  w+
#  r+  can not create a  new file --file must be present already
#  w+  always create a  new file first then do the rest


#  now time for  append mode

f=open('/tmp/shubhdha1.txt','a')
f.write("\n")
f.write("hii heros")
f.seek(0)
f.write("appending again ")
f.close()

# there is no read operation possible in  a mode 
#  use  a+  to append and read both 





