#importamos la libreria
import socket

#Creamos el socket, o la instancia del socket
SocketServidor = socket.socket()

#Nos conectamos al localhost o nos conectamos a la misma direccion del servidor
SocketServidor.connect(("localhost", 9999))

print("--- MENU ---")
print("Precione a para saludar")
print("Precione b para despedir")
print("Precione c para salir")
print("--- FIN ---\n")

#Creamos el ciclo para enviar peticiones al servidor
while True:
    #Solicitamos algo para enviar
    mensaje = input("> ")

    #Enviamos el prompt
    SocketServidor.send(bytes(mensaje,"utf-8"))

    #Si enviamos el mensaje para salir
    if(mensaje == "salir"):
        break

#Si el mensaje de salida es llamado
print("El cliente ha finalizado")

#Se cierra la conexion
SocketServidor.close()


