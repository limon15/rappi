from re import match

def alertar_error(campo, msg_adicional = ''):
    return print("El valor ingresado para '{0}' no es valido. {1}{2}Intente nuevamente.".format(campo, msg_adicional, '\n' if msg_adicional else ''))

def no_existe_en_lista(cadena, campo, lista_datos):
    return cadena.upper() not in [dic[campo] for dic in lista_datos]

def nombre_tiene_formato_valido(nombre):
    return bool(match('^[A-Za-z0-9 áéíóúÁÉÍÓÚñÑ]+$', nombre))

def precio_tiene_formato_valido(precio):
    return bool(match('^[0-9.]{1,7}$', precio))

def telefono_tiene_formato_valido(telefono):
    # /^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$/
    return bool(match('^[0-9 -_+()]+$', telefono))

def direccion_tiene_formato_valido(direccion):
    return bool(match('^[A-Za-z0-9-_°, áéíóúÁÉÍÓÚñÑ]+$', direccion))

def latitud_tiene_formato_valido(latitud):
    return bool(match('^[+-]?(([1-8]?[0-9])(\.[0-9]{1,6})?|90(\.0{1,6})?)$', latitud))

def longitud_tiene_formato_valido(longitud):
    return bool(match('^[+-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]{1,6})?)|180(\.0{1,6})?)$', longitud))

def radio_de_entrega_tiene_formato_valido(radio_de_entrega):
    return bool(match('^[0-9]{1,2}([.])*([0-9]{1,2})*$', radio_de_entrega))

def usuario_tiene_formato_valido(usuario):
    return bool(match('^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ]+$', usuario))

def contraseña_tiene_formato_valido(contraseña):
    return bool(match('^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,}$', contraseña))

def tiene_longitud_valida(campo, min, max):
    return min<=len(campo)<=max

def parentesis_balanceados(cadena): 
    parentesis_abre = '('
    parentesis_cierra = ')'
    pila = []
    dic_parentesis = { parentesis_abre: parentesis_cierra }
    for caracter in cadena:
        if caracter == parentesis_abre:
            pila.append(dic_parentesis[caracter])
        elif caracter == parentesis_cierra:
            if not pila or caracter != pila.pop():
                return False                
    return not pila

def restaurante_elegido_es_correcto(restaurantes, eleccion):
    revalidacion = "La eleccion elegida fue: {}. Si es correcto escriba 'si' de lo contrario escriba 'no': ".format(restaurantes[eleccion]['Nombre'])
    return True if revalidacion.upper() == 'SI' else False

# print(parentesis_balanceados("(011)) 4293-6406"))

# def validar_lat_long(latitud, longitud):
    # return not bool(match('^[0-9.]{1,7}$', latitud)) or not bool(match('^[0-9.]{1,7}$', latitud))    