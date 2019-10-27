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

def alertar_error(campo, msg_adicional = ''):
    return print("El valor ingresado para '{0}' no es valido. {1}{2}Intente nuevamente.".format(campo, msg_adicional, '\n' if msg_adicional else ''))

# Constantes de mensajes para inputs:

msg_nombre = "Ingrese un nombre o aprete * para volver atras: "    
msg_precio = "Ingrese el precio (decimales separados por '.'): "