# Sockets

## Para servidor
```py
import socket

puerto = 1337
ip = "0.0.0.0" # al poner un ip de 0.0.0.0 nos va a conectar a todo. Si damos un ip nos va a dar ese especifico

#Sock_STREAM es TCP y SOCK_DGRAM es UDP
#Mayusculas para alias de variables constantes finita para que no se modifique 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cualquier interfaz de la computadira 
s.bind((ip, puerto))

#Para encontrar una conexión 
s.listen(1) # el 1 significa que solo acepta una coneccion en total

#conn - El objeto de coneccion. Visto mas enfrente que puedes hacer
#addr - Direccion con quien se conecto
conn, addr = s.accept() 
with conn:
    data = conn.recv(1024)
    print(data.decode("ascii")) #estoy recibiendo ascii
    conn.send(b"hola") #b para cmabiar los datos a binario
    conn.close()

```

## Para cliente

```py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Decirle que se conecta a cierta IP al Puerto Fuente (esta en server.py)
s.connect(("192.168.1.11", 1337)) #El puerto destino será aleatorio

data = s.recv(1024)
print(data.decode("ascii"))
s.close()
```