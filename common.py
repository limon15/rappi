# msg_eleccion = "La eleccion elegida fue: {}. Si es correcto escriba 'si' de lo contrario escriba 'no': ".format(restaurantes[eleccion]['Nombre'])

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

