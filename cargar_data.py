from re import match
from validaciones import *
from prettytable import PrettyTable
from random import choice
from common import devolver_opcion_elegida_validada_desde_lista, listar_opciones, imprimir_aviso_de_retorno_al_menu_anterior, obtener_lista_nombres_restaurantes, evaluar_existencia_entidad
from info_predefinida import cargar_data_predefinida

# Constantes de inputs:

msg_nombre = "Ingrese un nombre o aprete * para volver atras: "
msg_precio = "Ingrese el precio (decimales separados por '.'): "
msg_direccion = "Ingrese una direccion: "
msg_telefono = "Ingrese un telefono: "
msg_latitud = "Ingrese la latitud de la direccion: "
msg_longitud = "Ingrese la longitud de la direccion: "
msg_radio_de_entrega = "Ingrese el radio de entrega del restaurante (en KM): "
msg_usuario = "Ingrese un nombre de usuario (numeros y/o letras sin espacios sin distincion de mayusculas) o aprete * para volver atras: "
msg_contraseña = "Ingrese una contraseña: "


def obtener_reporte_de_carga(cant_inicial, cant_final, cant_fallados, entidad):
    cant_nuevos = cant_final-cant_inicial
    t = PrettyTable(['CANT. INICIAL', 'CANT. FINAL', 'CANT. NUEVOS', 'CANT. FALLADOS*'])
    t.add_row([cant_inicial, cant_final, cant_nuevos, cant_fallados])
    return print("REPORTE DE CARGA DE {}: \n{}{}\n".format(entidad.upper(), t, "\n* El nombre a cargar se encontraba entre los ya existentes" if cant_fallados>0 else ''))

def imprimir_titulo_submenu(entidad):
    print("\n||   ALTA DE {}   ||\n".format(entidad).upper())   

def notificar_carga_exitosa(entidad, id):
    print("\nLa carga del {} '{}' se ha realizado correctamente\n".format(entidad, id))   

def pedir_direccion():
    direccion = input(msg_direccion)
    while not direccion_tiene_formato_valido(direccion):
        direccion = input(msg_direccion)
        alertar_error("direccion", "El valor ingresado no debe ser vacio.")
    return direccion

def pedir_telefono():
    telefono = input(msg_telefono)
    while not (telefono_tiene_formato_valido(telefono) and parentesis_balanceados(telefono)):
        alertar_error("telefono", "Ingrese solo numeros, espacios, guiones, '+' y parentesis.")
        telefono = input(msg_telefono)
    return telefono

def pedir_latitud():
    latitud = input(msg_latitud)
    while not latitud_tiene_formato_valido(latitud):
        alertar_error("latitud", "Ingrese solo numeros entre -90 y 90 (decimales separados por '.').")
        latitud = input(msg_latitud)
    return latitud

def pedir_longitud():
    longitud = input(msg_longitud)            
    while not longitud_tiene_formato_valido(longitud):
        alertar_error("longitud", "Ingrese solo numeros entre -180 y 180 (decimales separados por '.').")
        longitud = input(msg_longitud)
    return longitud

def pedir_radio_de_entrega():
    radio_de_entrega = input(msg_radio_de_entrega)
    while not radio_de_entrega_tiene_formato_valido(radio_de_entrega):
        alertar_error("radio de entrega", "Ingrese solo numeros positivos (decimales separados por '.').")
        radio_de_entrega = input(msg_radio_de_entrega)
    return radio_de_entrega

def pedir_contraseña():
    contraseña = input(msg_contraseña)
    while not contraseña_tiene_formato_valido(contraseña):
        alertar_error("contraseña", "Debe tener 8 caracteres con al menos un digito, una mayuscula, una minuscula y un caracter especial.")            
        contraseña = input(msg_contraseña)
    return contraseña

def pedir_precio():
    precio = input(msg_precio)
    while not precio_tiene_formato_valido(precio):
        alertar_error("precio", "\n a) No es un numero positivo. \n b) Tiene caracteres incorrectos para el indicio de decimal, utilice '.'. \n c) No se encuentra entre 0 y 9999.")           
        precio = input(msg_precio)
    return precio

# Cargar 
def cargar_nuevo_restaurante(lista_restaurantes=[]):
    imprimir_titulo_submenu("restaurante")
    nombre = input(msg_nombre)
    while nombre!='*':
        if (no_existe_en_lista(nombre, 'Nombre', lista_restaurantes) and nombre_tiene_formato_valido(nombre) and tiene_longitud_valida(nombre, 5, 25)):
            direccion = pedir_direccion()
            telefono = pedir_telefono()
            latitud = pedir_latitud()
            longitud = pedir_longitud()
            radio_de_entrega = pedir_radio_de_entrega()
            print("Ingrese los platos del restaurante '{}': ".format(nombre))    
            platos = cargar_nuevo_plato()
            lista_restaurantes.append({'Nombre': nombre.upper(), 'Direccion': direccion, 'Telefono': telefono, 'Posicion': (float(latitud), float(longitud)), 'Radio de entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas': 0.0, 'Moneda': 'ARG'})
            notificar_carga_exitosa("restaurante", nombre)   
        else:
            alertar_error("nombre", "\n a) Coincide con un restaurante existente. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_restaurantes   

def cargar_nuevo_plato():
    lista_de_platos = []
    imprimir_titulo_submenu("plato")
    nombre = input(msg_nombre)
    while nombre!='*':
        if (no_existe_en_lista(nombre, 'Nombre', lista_de_platos) and nombre_tiene_formato_valido(nombre) and tiene_longitud_valida(nombre, 5, 25)):
            precio = pedir_precio()
            lista_de_platos.append({'Nombre': nombre.upper(), 'Precio': round(float(precio),2)})
            notificar_carga_exitosa("plato", nombre)   
        else:
            alertar_error("nombre", "\n a) Coincide con un plato existente en el restaurante. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    return lista_de_platos  

def cargar_nuevo_cliente(lista_clientes=[]):
    imprimir_titulo_submenu("clientes")
    usuario = input(msg_usuario)
    while usuario!='*':
        if (no_existe_en_lista(usuario, 'Nombre de usuario', lista_clientes) and usuario_tiene_formato_valido(usuario) and tiene_longitud_valida(usuario, 3, 12)):
            contraseña = pedir_contraseña()
            telefono = pedir_telefono()
            direccion = pedir_direccion()
            latitud = pedir_latitud()
            longitud = pedir_latitud()
            lista_clientes.append({'Nombre de usuario': usuario.upper(), 'Contraseña': contraseña, 'Telefono': telefono, 'Direccion': direccion, 'Posicion': (float(latitud), float(longitud)), 'Rappicreditos': 0.0 })
            notificar_carga_exitosa("cliente", usuario)       
        else:
            alertar_error("usuario", "\n a) Coincide con un cliente existente. \n b) Tiene una longitud indebida (permitido entre 3 y 12 caracteres) \n c) Contiene espacios.")
        usuario = input(msg_usuario)
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes

def cargar_nuevo_rappitendero(lista_restaurantes=[], lista_rappitenderos=[]):
    existen_restaurantes = evaluar_existencia_entidad(lista_restaurantes, "restaurantes")
    if existen_restaurantes:
        imprimir_titulo_submenu("rappitendero")
        nombre = input(msg_nombre)
        while nombre!='*':
            if (nombre_tiene_formato_valido(nombre)):            
                posicion_actual = choice(lista_restaurantes)['Posicion actual']
                lista_rappitenderos.append({'Nombre': nombre.upper(), 'Propina acumulada': 0.0, 'Posicion actual': posicion_actual, 'Pedido actual': None})
                notificar_carga_exitosa("rappitendero", nombre)            
            else:
                alertar_error("nombre", "\n a) No tiene un formato valido.")
            nombre = input(msg_nombre)
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_rappitenderos

def validar_nombre_eleccion_entidad(eleccion, entidad):
    validar_eleccion = input("La elección realizada fue '{}'. Si es correcto ingrese 'si' o ingrese cualquier caracter para volver: ".format(entidad[eleccion]['Nombre'].upper()))
    return True if validar_eleccion.upper() == 'SI' else False

def actualizar_platos_restaurante(lista_restaurantes):
    existen_restaurantes = evaluar_existencia_entidad(lista_restaurantes, "restaurantes")
    if existen_restaurantes:
        opcion_validada = False
        while not opcion_validada:
            print("\n\t\tElija el restaurante para el cual desea cargar el plato:\n")     
            nombres_restaurantes = obtener_lista_nombres_restaurantes(lista_restaurantes)
            opcion_elegida = devolver_opcion_elegida_validada_desde_lista(nombres_restaurantes, 3)
            opcion_validada = validar_nombre_eleccion_entidad(opcion_elegida, lista_restaurantes)
        lista_restaurantes[opcion_elegida]['Platos'].extend(cargar_nuevo_plato())
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_restaurantes

def carga_manual(lista_clientes, lista_restaurantes, lista_rappitenderos):
    opciones = ["Cargar un nuevo restaurante.",  "Cargar un nuevo plato.", "Cargar un nuevo cliente.", "Cargar un nuevo rappitendero.", "Volver al menu anterior."]
    tabulacion = 2
    opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, tabulacion)
    volver = len(opciones)-1    
    while opcion_elegida != volver:
        if (opcion_elegida == 0):
            lista_restaurantes = cargar_nuevo_restaurante(lista_restaurantes)     
        elif (opcion_elegida == 1):
            lista_restaurantes = actualizar_platos_restaurante(lista_restaurantes)
        elif (opcion_elegida == 2):
            lista_clientes = cargar_nuevo_cliente(lista_clientes)                     
        elif (opcion_elegida == 3):
            lista_rappitenderos = cargar_nuevo_rappitendero(lista_rappitenderos) 
        opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, tabulacion)
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes, lista_restaurantes, lista_rappitenderos 


def carga_predefinida(lista_clientes=[], lista_restaurantes=[], lista_rappitenderos=[]):
    lista_clientes = cargar_data_predefinida(lista_clientes, 'clientes')
    lista_restaurantes = cargar_data_predefinida(lista_restaurantes,'restaurantes')
    lista_rappitenderos = cargar_data_predefinida(lista_rappitenderos, 'rappitenderos')
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes, lista_restaurantes, lista_rappitenderos