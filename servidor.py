import socket

#Crear o instancear un objeto socket
SocketServidor = socket.socket()
print("Socket listo")
print(SocketServidor)
#input()

#Conectamos el servidor a un puerto o lo bindeamos a un puerto
SocketServidor.bind(("localhost", 8888))
print("Conectado a localhost en el puerto 8888")

#Escuchamos conexiones entrantes al servidor
SocketServidor.listen(1)
print("Escuchando en puerto 8888")

#Aceptando peticiones entrantes
SocketCliente, addr = SocketServidor.accept()
print("Informacion Socket cliente: ", SocketCliente)
print(addr)
print("Acepta peticion entrante")

while True:
    recibidoCliente = SocketCliente.recv(1024)
    mensaje = recibidoCliente.decode("utf-8")

    if(mensaje == "salir"):
        break
    elif(mensaje == 'a'):
        cantidadRecibida = SocketCliente.recv(1024)
        cantidadMonetaria = int(cantidadRecibida.decode("utf-8"))

        calculoEuro = cantidadMonetaria * 890

        resultadoA = str(calculoEuro)

        SocketCliente.send(bytes(resultadoA, "utf-8"))
        print("Cantidad Enviada")
    elif(mensaje == 'b'):
        cantidadRecibida = SocketCliente.recv(1024)
        cantidadMonetaria = int(cantidadRecibida.decode("utf-8"))

        calculoEuro = cantidadMonetaria * 771

        resultadoA = str(calculoEuro)

        SocketCliente.send(bytes(resultadoA, "utf-8"))
        print("Cantidad Enviada")


print("Conexion Finalizada")

SocketCliente.close()
SocketServidor.close()