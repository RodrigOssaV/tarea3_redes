# tarea3_redes

Tarea sobre el funcionamiento de Socket con un ejemplo de cliente - servidor.

Aplicación basado en servicio Cliente/Servidor de cambio de dividas (Chilenas a internacional)

Integrantes de la aplicación

Diego Sanhueza

Rodrigo Ossa


# Manual de Usuario

A continuación se presentan dos casos,
Primer caso, que los archivos y procedimientos de la tarea 3 se encuentren
implementados en la maquina virtual, cuyo procedimiento es el siguiente:

# Caso Implementado en maquina virtual

Paso 1) Ejectuar una ventana de terminal (ubuntu) el servidor, colocar el comando a continuacion,
notar que se esta ejecutando en python 3.8, ya añadido en la maquina virtual

>> python3.8 servidor.py

Paso 2) Ejectuar una ventana de terminal (ubuntu) el cliente, colocar el comando a continuacion:

>> python3.8 cliente.py

Paso 3) Se dará cuenta que el programa comienza a funcionar y se despliega un menu con opciones,
varios cambios de divisa a pesos chilenos, seleccione mediante las letras (opciones) un cambio de divisa
y presione enter, a continuacion se enviara el codigo al servidor que retornará una respuesta como la siguiente:

>> La Cantidad Convertida es:  890000

Q: Notar que si la cantidad ingresada en la opcion 'a' Euros a pesos chilenos es de €1000 euros, la cantidad en 
pesos chilenos es de $890.000 aprox.

Finalmente el programa vuelve a desplegar el menu para repetir el proceso, si no desea continuar, puede escribir
en pantalla la opcion "salir" todo en minusculas para terminar la conexión.

# Caso No implementado en maquina virtual

Los siguientes procedimientos son identicos a los procedimientos del caso implementado en la maquina virtual
con la diferencia que, en windows, se ejecuta la consola de windows (cmd) en modo administrador para evitar errores 
y se ejecuta el paso 1 y 2 con los comandos "py" en vez de "python3.8" como muestra a continuación:

>> py servidor.py

>> py cliente.py

Es necesario tener la version python 3.8 en windows como tambien en la maquina virtual.

