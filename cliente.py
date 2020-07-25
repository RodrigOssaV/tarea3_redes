import socket

import time

SocketServidor = socket.socket()

#Nos conectamos al localhost o nos conectamos a la misma direccion del servidor
SocketServidor.connect(("localhost", 8888))

while True:
    print("//////////////   MENU   /////////////////")
    print("Escriba 'salir' para terminar la conexión")
    print("a) EUR to CLP")
    print("b) USD to CLP")
    print("c) JPY to CLP")
    print("d) ARS to CLP")
    print("e) GBP to CLP")
    print("f) BRL to CLP")
    print("\n")
    #data = input("(Opción)>> ")

    while True:
        data = input("(Opción)>> ")

        if(data == "salir"):
            break

        if((data == 'a') or (data == 'b') or (data == 'c') or (data == 'd') or (data == 'e') or (data == 'f')):
            break
        else:
            print("\n")
            print('Error, la opción es incorrecta, vuelva a intentarlo')

    #TODO Validar entradas

    if(data == "salir"):
        SocketServidor.send(bytes(data, "utf-8"))
        break
    SocketServidor.send(bytes(data, "utf-8"))

    cantidadEnviar = input("(Cantidad)>> ")
    SocketServidor.send(bytes(cantidadEnviar, "utf-8"))

    cantidadRecibida = SocketServidor.recv(1024)
    cantidadConvertida = cantidadRecibida.decode("utf-8")

    print("\n")
    print("La Cantidad Convertida es: ",cantidadConvertida) 

    time.sleep(2)


print("El cliente ha finalizado")

#Se cierra la conexion
SocketServidor.close()

