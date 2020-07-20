#Importar la libreria
import socket

#importamos las funciones de conversion
import cambioMoneda

#Crear o instancear un objeto socket
SocketServidor = socket.socket()
print("Socket listo")
print(SocketServidor)
#input()

#Conectamos el servidor a un puerto o lo bindeamos a un puerto
SocketServidor.bind(("localhost", 9999))
print("Conectado a localhost en el puerto 9999")

#Escuchamos conexiones entrantes al servidor
SocketServidor.listen(1)
print("Escuchando en puerto 9999")

#Aceptando peticiones entrantes
SocketCliente, addr = SocketServidor.accept()
print("Informacion Socket cliente: ", SocketCliente)
print(addr)
print("Acepta peticion entrante")

#se ejecuta un ciclo para recibir peticiones del cliente
while True:

    #Recibimos la opcion del cliente
    dataEntrante = SocketCliente.recv(1024)
    mensaje = dataEntrante.decode("utf-8")

    #---------Funcion para salir------------
    if mensaje  == "salir":
        break
    #---------------------------------------

    #---------TO DO las funciones para convertir divisas----------
    #---------Agregarle switch------------------------------------
    if(mensaje == 'a'):
        cantidadAConvertir = SocketCliente.recv(1024)
        retorno = cambioMoneda.euro_clp(cantidadAConvertir)
        SocketCliente.send(retorno) #.encode("utf-8"))
    elif(mensaje == "b"):
        retorno = cambioMoneda.euro_clp("hola mundo")
        SocketCliente.sendall(retorno.encode("utf-8"))
    elif(mensaje == "c"):
        retorno = cambioMoneda.euro_clp("hola mundo")
        SocketCliente.sendall(retorno.encode("utf-8"))
     #------------------------------------------------------------

    #print ("recibido:", mensaje)

#Terminar conexion
print("Conexion Finalizada")

SocketCliente.close()
SocketServidor.close()