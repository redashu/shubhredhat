#!/usr/bin/python

import  socket
rec_ip="172.17.0.4"
rec_port=8899

#  creating  socket 
#          ipveriosn , protocol type--UDP  

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# binding  ip and port 

s.bind((rec_ip,rec_port))

while  True:
	print  s.recvfrom(100)



