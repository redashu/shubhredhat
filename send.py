#!/usr/bin/python

import  socket,time
#  also created  UDP socket 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  we need to send data to receiver 

while True:
	x=raw_input("type your message :  ")	
	s.sendto(x,("172.17.0.4",8899))
	time.sleep(2)


