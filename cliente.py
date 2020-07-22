import socket

SocketServidor = socket.socket()

#Nos conectamos al localhost o nos conectamos a la misma direccion del servidor
SocketServidor.connect(("localhost", 8888))

while True:
    print("MENU")
    print("a) Euro a Clp")
    print("b) Dolar a Clp")
    print("c) Yen a Clp")
    print("\n")

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

    print("\n")
    print("La Cantidad Convertida es: ",cantidadConvertida) 
    print("\n")


print("El cliente ha finalizado")

#Se cierra la conexion
SocketServidor.close()

