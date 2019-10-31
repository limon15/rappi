from re import match
from validaciones import *
from prettytable import PrettyTable
from random import choice
from common import devolver_opcion_elegida_validada_desde_lista, listar_opciones, imprimir_aviso_de_retorno_al_menu_anterior, obtener_lista_nombres_restaurantes, evaluar_existencia_entidad

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

# Data harcodeada: 
def cargar_restaurantes_predefinidos(lista_restaurantes=[]):
    cant_inicial = len(lista_restaurantes)
    cant_fallados = 0
    restaurantes = [
        {'Nombre': 'MARIA BONITA', 'Direccion': 'Mitre 1195, Adrogue, Buenos Aires', 'Telefono': '011 4294-1184', 'Posicion': (-34.797054, -58.391627), 'Radio de entrega': 2.5, 'Platos': [{'Nombre': 'Ensalada Ninetta', 'Precio': 250},{'Nombre': 'Rissotto ai funghi', 'Precio': 370}, {'Nombre': 'Brotola a los 4 quesos', 'Precio': 570}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PASTA ROSSA', 'Direccion': 'Jorge San Pellerano 754, Adrogue, Buenos Aires', 'Telefono': '011 4214-3437', 'Posicion': (-34.799433, -58.390941), 'Radio de entrega': 1, 'Platos': [{'Nombre': 'Gnocchi souffle', 'Precio': 219},{'Nombre': 'Ravioli di formaggio', 'Precio': 229}, {'Nombre': 'Sorrentino di salmone', 'Precio': 310}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PIZZERIA EL FARO', 'Direccion': 'Esteban Adrogué 1187, Adrogue, Buenos Aires', 'Telefono': '011 4214-4144', 'Posicion': (-34.798170, -58.390783), 'Radio de entrega': 3.5, 'Platos': [{'Nombre': 'Pizza muzzarella', 'Precio': 150},{'Nombre': 'Pizza napolitana', 'Precio': 170}, {'Nombre': 'Pizza ananá con azucar', 'Precio': 200}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'TIRIFILO EL BODEGON', 'Direccion': 'Cordero 694, Adrogue, Buenos Aires', 'Telefono': '011 4294-4195', 'Posicion': (-34.801080, -58.395488), 'Radio de entrega': 5, 'Platos': [{'Nombre': 'Milanesa con ensalada', 'Precio': 200},{'Nombre': 'Salteado de carne', 'Precio': 250}, {'Nombre': 'Guiso de mondongo', 'Precio': 320}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'SUSHI ADROGUE', 'Direccion': 'Int. Dr. Martín González 806, Adrogue, Buenos Aires', 'Telefono': '0810-220-2006', 'Posicion': (-34.798375, -58.396260), 'Radio de entrega': 0.5, 'Platos': [{'Nombre': 'Uramaki', 'Precio': 300},{'Nombre': 'Nirigi de atun', 'Precio': 350}, {'Nombre': 'Dorayakis', 'Precio': 400}], 'Total de ventas': 0, 'Moneda': 'ARG'}]
    if (cant_inicial!=0):
        for dic in restaurantes:
            if (no_existe_en_lista(dic['Nombre'], 'Nombre', lista_restaurantes)):
                lista_restaurantes.extend([dic])
            else:
                cant_fallados+=1    
    else:
        lista_restaurantes = restaurantes
    cant_final = len(lista_restaurantes)
    obtener_reporte_de_carga(cant_inicial, cant_final, cant_fallados, 'restaurantes')
    return lista_restaurantes


def cargar_clientes_predefinidos(lista_clientes=[]):
    cant_inicial = len(lista_clientes)
    cant_fallados = 0
    clientes = [
        {'Nombre de usuario': 'LUCHIA31', 'Contraseña': 'Buonabitacolo31!', 'Telefono': '011 4214-7576', 'Direccion': 'Erezcano 1576, Adrogue, Buenos aires', 'Posicion': (-34.802668, -58.375369), 'Rappicreditos': 0},
        {'Nombre de usuario': '2019AMARIAG', 'Contraseña': 'nuncioYana2019?', 'Telefono': '011 4214-7576', 'Direccion': 'Av. Espora 200, Adrogué, Buenos aires', 'Posicion': (-34.788542, -58.389000), 'Rappicreditos': 0},
        {'Nombre de usuario': 'BESTCATEVER', 'Contraseña': '#onlyFood17', 'Telefono': '011 4293-6406', 'Direccion': 'King 725, José Mármol, Buenos aires', 'Posicion': (-34.789540, -58.373989), 'Rappicreditos': 0},
        {'Nombre de usuario': 'RAULO1', 'Contraseña': 'Radiopa$ion1929', 'Telefono': '011 4293-1833', 'Direccion': 'Benigno Macias 443, Adrogue, Buenos aires', 'Posicion': (-34.797054, -58.391627), 'Rappicreditos': 0},
        {'Nombre de usuario': 'FLEQUI26', 'Contraseña': 'lamunil*CA1', 'Telefono': '011 4294-3936', 'Direccion': 'Cerretti 876, Adrogue, Buenos aires', 'Posicion': (-34.799099, -58.386906), 'Rappicreditos': 0}
        ]
    if (cant_inicial!=0):
        for dic in clientes:
            if (no_existe_en_lista(dic['Nombre de usuario'], 'Nombre de usuario', lista_clientes)):
                lista_clientes.extend([dic])
            else:
                cant_fallados+=1                    
    else:
        lista_clientes = clientes
    cant_final = len(lista_clientes)
    obtener_reporte_de_carga(cant_inicial, cant_final, cant_fallados, 'clientes')      
    return lista_clientes

def cargar_rappitenderos_predefinidos(lista_rappitenderos=[]):
    cant_inicial = len(lista_rappitenderos)
    cant_fallados = 0
    rappitenderos = [
        {'Nombre': 'LUCIANA ARCOIRIS', 'Propina acumulada': 0, 'Posicion actual': (-34.789540, -58.373989), 'Pedido actual': None},
        {'Nombre': 'JONATHAN MOREL', 'Propina acumulada': 0, 'Posicion actual': (-34.797054, -58.391627), 'Pedido actual': None},
        {'Nombre': 'AURELIANO OLIVA', 'Propina acumulada': 0, 'Posicion actual': (-34.799099, -58.386906), 'Pedido actual': None},
        {'Nombre': 'ATENEA ANTI', 'Propina acumulada': 0, 'Posicion actual': (-34.788542, -58.389000), 'Pedido actual': None},
        {'Nombre': 'MORFI MOCHUELO', 'Propina acumulada': 0, 'Posicion actual': (-34.802668, -58.375369), 'Pedido actual': None}
    ]
    if (cant_inicial!=0):
        for dic in rappitenderos:
            if (no_existe_en_lista(dic['Nombre'], 'Nombre', lista_rappitenderos)):
                lista_rappitenderos.extend([dic])
            else:
                cant_fallados+=1                
    else:
        lista_rappitenderos = rappitenderos
    cant_final = len(lista_rappitenderos)
    obtener_reporte_de_carga(cant_inicial, cant_final, cant_fallados, 'rappitenderos')         
    return lista_rappitenderos

# Cargar 
def cargar_nuevo_restaurante(lista_restaurantes=[]):
    nombre = input(msg_nombre)
    while nombre!='*':
        if (no_existe_en_lista(nombre, 'Nombre', lista_restaurantes) and nombre_tiene_formato_valido(nombre) and tiene_longitud_valida(nombre, 5, 25)):
            direccion = input(msg_direccion)
            while not direccion_tiene_formato_valido(direccion):
                alertar_error("direccion", "El valor ingresado no debe ser vacio.")
                direccion = input(msg_direccion)
            telefono = input(msg_telefono)
            while not (telefono_tiene_formato_valido(telefono) and parentesis_balanceados(telefono)):
                alertar_error("telefono", "Ingrese solo numeros, espacios, guiones, '+' y parentesis.")
                telefono = input(msg_telefono)
            latitud = input(msg_latitud)
            while not latitud_tiene_formato_valido(latitud):
                alertar_error("latitud", "Ingrese solo numeros entre -90 y 90 (decimales separados por '.').")
                latitud = input(msg_latitud)
            longitud = input(msg_longitud)            
            while not longitud_tiene_formato_valido(longitud):
                alertar_error("longitud", "Ingrese solo numeros entre -180 y 180 (decimales separados por '.').")
                longitud = input(msg_longitud)
            radio_de_entrega = input(msg_radio_de_entrega)
            while not radio_de_entrega_tiene_formato_valido(radio_de_entrega):
                alertar_error("radio de entrega", "Ingrese solo numeros positivos (decimales separados por '.').")
                radio_de_entrega = input(msg_radio_de_entrega)
            print("Ingrese los platos del restaurante '{}': ".format(nombre))    
            platos = cargar_nuevo_plato()
            lista_restaurantes.append({'Nombre': nombre.upper(), 'Direccion': direccion, 'Telefono': telefono, 'Posicion': (float(latitud), float(longitud)), 'Radio de entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas': 0.0, 'Moneda': 'ARG'})            
        else:
            alertar_error("nombre", "\n a) Coincide con un restaurante existente. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    return lista_restaurantes   

def cargar_nuevo_plato():
    lista_de_platos = []
    nombre = input(f'\tmsg_nombre')
    while nombre!='*':
        if (no_existe_en_lista(nombre, 'Nombre', lista_de_platos) and nombre_tiene_formato_valido(nombre) and tiene_longitud_valida(nombre, 5, 25)):
            precio = input(msg_precio)
            while not precio_tiene_formato_valido(precio):
                alertar_error("precio", "\n a) No es un numero positivo. \n b) Tiene caracteres incorrectos para el indicio de decimal, utilice '.'. \n c) No se encuentra entre 0 y 9999.")           
                precio = input(msg_precio)
            lista_de_platos.append({'Nombre': nombre.upper(), 'Precio': round(float(precio),2)})
        else:
            alertar_error("nombre", "\n a) Coincide con un plato existente en el restaurante. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    return lista_de_platos  

def cargar_nuevo_cliente(lista_clientes=[]):
    usuario = input(msg_usuario)
    while usuario!='*':
        if (no_existe_en_lista(usuario, 'Nombre de usuario', lista_clientes) and usuario_tiene_formato_valido(usuario) and tiene_longitud_valida(usuario, 3, 12)):
            contraseña = input(msg_contraseña)
            while not contraseña_tiene_formato_valido(contraseña):
                alertar_error("contraseña", "Debe tener 8 caracteres con al menos un digito, una mayuscula, una minuscula y un caracter especial.")            
                contraseña = input(msg_contraseña)
            telefono = input(msg_telefono)
            while not (telefono_tiene_formato_valido(telefono) and parentesis_balanceados(telefono)):
                alertar_error("telefono", "Ingrese solo numeros, espacios, guiones, '+' y parentesis.")
                telefono = input(msg_telefono)
            direccion = input(msg_direccion)                
            while not direccion_tiene_formato_valido(direccion):
                alertar_error("direccion", "El valor ingresado no debe ser vacio.")
                direccion = input(msg_direccion)                
            latitud = input(msg_latitud)
            while not latitud_tiene_formato_valido(latitud):
                alertar_error("latitud", "Ingrese solo numeros entre -90 y 90 (decimales separados por '.').")
                latitud = input(msg_latitud)
            longitud = input(msg_longitud)            
            while not longitud_tiene_formato_valido(longitud):
                alertar_error("longitud", "Ingrese solo numeros entre -180 y 180 (decimales separados por '.').")
                longitud = input(msg_longitud)
            lista_clientes.append({'Nombre de usuario': usuario.upper(), 'Contraseña': contraseña, 'Telefono': telefono, 'Direccion': direccion, 'Posicion': (float(latitud), float(longitud)), 'Rappicreditos': 0.0 })
        else:
            alertar_error("usuario", "\n a) Coincide con un cliente existente. \n b) Tiene una longitud indebida (permitido entre 3 y 12 caracteres) \n c) Contiene espacios.")
        usuario = input(msg_usuario)         
    return lista_clientes

def cargar_nuevo_rappitendero(lista_restaurantes=[]):
    lista_rappitenderos=[]
    if (len(lista_restaurantes)!=0):
        nombre = input(msg_nombre)
        while nombre!='*':
            if (nombre_tiene_formato_valido(nombre)):            
                posicion_actual = choice(lista_restaurantes)['Posicion actual']
                lista_rappitenderos.append({'Nombre': nombre.upper(), 'Propina acumulada': 0.0, 'Posicion actual': posicion_actual, 'Pedido actual': None})
            else:
                alertar_error("nombre", "\n a) No tiene un formato valido.")
            nombre = input(msg_nombre)                          
    else:
        print("Aun no se han cargado restaurantes. El rappitendero no puede ser creado.")         
    return lista_rappitenderos

def validar_nombre_eleccion_entidad(eleccion, entidad):
    validar_eleccion = input("La elección realizada fue '{}'. Si es correcto ingrese 'si' o ingrese cualquier caracter para volver: ".format(entidad[eleccion]['Nombre']))
    return True if validar_eleccion.upper() == 'SI' else False

def actualizar_platos_restaurante(lista_restaurantes):
    existen_restaurantes = evaluar_existencia_entidad(lista_restaurantes, "restaurantes")
    if existen_restaurantes:
        opcion_validada = False
        while not opcion_validada:
            print("\tElija el restaurante para el cual desea cargar el plato:\n")     
            nombres_restaurantes = obtener_lista_nombres_restaurantes(lista_restaurantes)
            opcion_elegida = devolver_opcion_elegida_validada_desde_lista(nombres_restaurantes)
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


def cargar_predefinida(lista_clientes=[], lista_restaurantes=[], lista_rappitenderos=[]):
    lista_clientes = cargar_clientes_predefinidos(lista_clientes)
    lista_restaurantes = cargar_restaurantes_predefinidos(lista_restaurantes)
    lista_rappitenderos = cargar_rappitenderos_predefinidos(lista_rappitenderos)
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes, lista_restaurantes, lista_rappitenderos