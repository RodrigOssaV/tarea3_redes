#Importamos el módulo socket
import socket

#Iniciamos un objeto servidor asociado a socket
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Método BIND: Conecta una dirección local a un socket
servidor.bind(("", 8050))

#Método LISTEN: Anuncia la disposición a aceptar conexiones; indica tamaño de cola.
servidor.listen(1)

#
cliente, direccion = servidor.accept()

while True:
    #Recibimos la respuesta del cliente.
    recibido = cliente.recv(1024)

    #Verificamos la conexión del cliente. 
    print "Recibo conexion de la IP: " + str(direccion[0]) + "Puerto: " + str(direccion[1])
    
    #Dependiendo de la respuesta del cliente, se desplegaran los siguientes mensajes.
    if(recibido == 'a'):
        #Mensaje que el servidor le mandara al cliente.
        mensaje_saludo = ("Hola Cliente")
        #Método SEND: Envía datos a través de la conexión.
        cliente.send(mensaje_saludo)
    elif(recibido == 'b'):
        mensaje_despedida = ("Adiós Cliente")
        cliente.send(mensaje_despedida)
    else:
        mensaje_conexion = ("Cerrando conexión")
        cliente.send(mensaje_conexion)
        #Cerramos las conexión con el cliente.
        cliente.close()
        
    #print(recibido)
    #cli.send("mensaje recibido")
    #msg_toSend = ("Mensaje recibido desde el cliente, como estás Jerry")
    #cliente.send(msg_toSend)

#cliente.close()
servidor.close()

print("Conexiones cerradas")
