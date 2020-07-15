#Importar la libreria
import socket

#Crear o instancear un objeto socket
SocketServidor = socket.socket()
print("Socket listo")
print(SocketServidor)
#input()

#Conectamos el servidor a un puerto
#Lo bindeamos a un puerto
SocketServidor.bind(("localhost", 9999))
print("Conectado a localhost en el puerto 9999")

#Escuchamos conexiones entrantes al servidor
SocketServidor.listen(1)
print("Escuchando en puerto 9999")

#Aceptando peticiones entrantes
SocketCliente, addr = SocketServidor.accept()
print(SocketCliente)
print(addr)
print("Acepta peticion entrante")

#se ejecuta un ciclo para recibir peticiones del cliente
while True:
    recibido = SocketCliente.recv(1024)
    if recibido.decode("utf-8") == "salir":
        break
    print ("recibido:", recibido.decode("utf-8"))

#Terminar conexion
print("Conexion Finalizada")

SocketCliente.close()
SocketServidor.close()
