import socket

puerto = 1337
ip = "192.168.1.12"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Decirle que se conecta a cierta IP al Puerto Fuente (esta en server.py)
s.connect((ip, puerto)) #El puerto destino será aleatorio

data = s.recv(1024)
print(data.decode("ascii"))
s.close()