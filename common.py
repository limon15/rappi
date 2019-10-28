# Constantes de mensajes para inputs:

msg_nombre = "Ingrese un nombre aprete * para volver atras: ",
msg_precio = "Ingrese el precio (decimales separados por '.'): ",
msg_direccion = "Ingrese una direccion: ",
msg_telefono = "Ingrese un telefono: ",  
msg_latitud = "Ingrese la latitud de la direccion: ",
msg_longitud = "Ingrese la longitud de la direccion: ",
msg_radio_de_entrega = "Ingrese el radio de entrega del restaurante (en KM): "

def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero referido a las opciones del menu: "))
            correcto = True
        except ValueError:
            print('Error. La opcion ingresada no es un numero entero.')
    return num

