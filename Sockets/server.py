import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 10000))
server.listen(1)

connection, address = server.accept()

while True:
	data = connection.recv(1024)
	if not data: break
	print "Data recieved: " + str(data)
connection.close()
