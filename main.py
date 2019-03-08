"""
Control de Sockets
Geovanny Gonzalez
"""

#Importar libreria socket
import socket

#Abrir conexión al servidor
sv_socket = socket.socket()

#Pasar dirección de despliegue, tupla, 0 es la IP, 1 es el puerto
sv_socket.bind(("localhost", 8083))

#Escuchar solo 1 conexion
sv_socket.listen(1)

#El elemento conexion es el socket que relaciona la conexion entre el cliente y el servidor, direccion la tupla con la
#direccion y puerto de escucha

cliente, direccion = sv_socket.accept()

#Procesar peticiones
trabajo = True
while trabajo:
    #Receive recibe un objeto Bytes, el cual toca interpretarlo de acuerdo a una codificacion
    bytes = cliente.recv(1024) #El 1024 es el tamanio en bits del buffer, implementacion Unix, ver documentacion
    recibido = bytes.decode('utf-8') #Se debe decodificar el mensaje a String
    print("Se ha recibido del cliente: ", recibido)
    if recibido == "Terminar" or len(recibido) == 0:
        trabajo = False
        cliente.send("Terminar".encode('utf-8')) #El paramtero deben ser objetos byte codificados
    #Utilizar el .send para contestar mensajes
    else:
        mensaje = recibido
        print("Enviando al cliente: ", mensaje)
        cliente.send(mensaje.encode('utf-8'))

#Cerrar conexiones, orden inverso
cliente.close()
sv_socket.close()





