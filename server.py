#!/usr/bin/env python3

import socket, select


TCP_IP = '172.31.81.158'
TCP_PORT = 5005
BUFFER_SIZE = 10  # Normally 1024, but we want fast response


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

try:
	print('Connection address:', addr)

	while True:
		command = ""

		while True:
			try:
				data = str(conn.recv(BUFFER_SIZE), 'utf-8')
				command += data
			except Exception:
				print("Error",data)
				pass
			if command[-3:] == ">>>":
				break
		print(command[:-3])

		command = input(">>> ")
		conn.send(bytes(command, 'utf-8'))
except KeyboardInterrupt:
	conn.close()
	print("Closing connection")
	
