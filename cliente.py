#importamos la libreria
import socket
import menu
import validador

#Creamos el socket, o la instancia del socket
SocketServidor = socket.socket()

#Nos conectamos al localhost o nos conectamos a la misma direccion del servidor
SocketServidor.connect(("localhost", 9999))


#Creamos el ciclo para enviar peticiones al servidor
while True:
    #Despliega el menu de opciones por pantalla
    menu.principal()

    #Instancia del mensaje fuera del loop (por razones logicas y flujo del programa)
    mensaje = ''

    #Entro a un loop para validar las opciones
    while True:
        mensaje = input("> ")

        if(mensaje == "salir"):
            break

        if(validador.validarDatos(mensaje) == True):
            break
        else:
            print(">> Opción Errónea, seleccione de nuevo")

    #Si la opcion es salir, el programa termina
    if(mensaje == "salir"):
        SocketServidor.send(bytes(mensaje,"utf-8"))
        break

    #Despliega instrucciones por pantalla
    menu.cantidad()

    cantidad = int(input("> Cantidad: "))

    #Enviamos el dato al servidor
    SocketServidor.send(bytes(cantidad,"utf-8"))

    #Recibimos respuesta del servidor (R: la cantidad ya procesada) 
    recibido = SocketServidor.recv(1024)
    print(recibido.decode("utf-8"))


#Si el mensaje de salida es llamado
print("El cliente ha finalizado")

#Se cierra la conexion
SocketServidor.close()

