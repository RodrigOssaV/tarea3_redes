# Variables a utilizar
localhost = 'localhost'
puerto = 8050

#Importamos el módulo socket
import socket

#Creamos el objeto socket
socket = socket.socket()

#Conexión con el servidor
socket.connect((localhost, puerto))

#Imprimimos el menu para interactuar con cliente
print("--- MENU ---")
print("Precione a para saludar")
print("Precione b para despedir")
print("Precione c para salir")
print("--- FIN ---\n")
     
#Creamos un bucle para retener la conexión
while True:
    #Entrada de datos para interactuar con cliente
    mens = raw_input("Su respuesta >> ")

    #Método send envia mensaje
    socket.send(mens.encode('ascii'))

    #Método recv recibe mensaje del servidor
    recibido = socket.recv(1024)
    print(recibido)

#Cerramos la instancia del servidor.
socket.close()
print("Conexión cerrada")
