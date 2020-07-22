import socket

import time

SocketServidor = socket.socket()

#Nos conectamos al localhost o nos conectamos a la misma direccion del servidor
SocketServidor.connect(("localhost", 8888))

while True:
    print("MENU")
    print("a) EUR to CLP")
    print("b) USD to CLP")
    print("c) JPY to CLP")
    print("d) ARS to CLP")
    print("e) GBP to CLP")
    print("f) BRL to CLP")
    print("\n")
    data = input("(Opción)>> ")

    data = input("(Opción)>> ")

    #TODO Validar entradas

    if(data == "salir"):
        SocketServidor.send(bytes(data, "utf-8"))
        break
    SocketServidor.send(bytes(data, "utf-8"))

    cantidadEnviar = input("(Cantidad)>> ")
    SocketServidor.send(bytes(cantidadEnviar, "utf-8"))

    cantidadRecibida = SocketServidor.recv(1024)
    cantidadConvertida = cantidadRecibida.decode("utf-8")

    print("La Cantidad Convertida es: ",cantidadConvertida) 
    print("\n")
    time.sleep(3)


print("El cliente ha finalizado")

#Se cierra la conexion
SocketServidor.close()

