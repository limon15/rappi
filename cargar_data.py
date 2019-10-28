from re import match
from validaciones import *

# Constantes de inputs:

msg_nombre = "Ingrese un nombre aprete * para volver atras: ",
msg_precio = "Ingrese el precio (decimales separados por '.'): ",
msg_direccion = "Ingrese una direccion: ",
msg_telefono = "Ingrese un telefono: ",  
msg_latitud = "Ingrese la latitud de la direccion: ",
msg_longitud = "Ingrese la longitud de la direccion: ",
msg_radio_de_entrega = "Ingrese el radio de entrega del restaurante (en KM): "


# Data harcodeada: 
def cargar_restaurantes():
    restaurantes = [
        {'Nombre': 'MARIA BONITA', 'Direccion': 'Mitre 1195, Adrogue, Buenos Aires', 'Telefono': '011 4294-1184', 'Posicion': (-34.797054, -58.391627), 'Radio de entrega': 2.5, 'Platos': [{'Nombre': 'Ensalada Ninetta', 'Precio': 250},{'Nombre': 'Rissotto ai funghi', 'Precio': 370}, {'Nombre': 'Brotola a los 4 quesos', 'Precio': 570}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PASTA ROSSA', 'Direccion': 'Jorge San Pellerano 754, Adrogue, Buenos Aires', 'Telefono': '011 4214-3437', 'Posicion': (-34.799433, -58.390941), 'Radio de entrega': 1, 'Platos': [{'Nombre': 'Gnocchi souffle', 'Precio': 219},{'Nombre': 'Ravioli di formaggio', 'Precio': 229}, {'Nombre': 'Sorrentino di salmone', 'Precio': 310}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PIZZERIA EL FARO', 'Direccion': 'Esteban Adrogué 1187, Adrogue, Buenos Aires', 'Telefono': '011 4214-4144', 'Posicion': (-34.798170, -58.390783), 'Radio de entrega': 3.5, 'Platos': [{'Nombre': 'Pizza muzzarella', 'Precio': 150},{'Nombre': 'Pizza napolitana', 'Precio': 170}, {'Nombre': 'Pizza ananá con azucar', 'Precio': 200}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'TIRIFILO EL BODEGON', 'Direccion': 'Cordero 694, Adrogue, Buenos Aires', 'Telefono': '011 4294-4195', 'Posicion': (-34.801080, -58.395488), 'Radio de entrega': 5, 'Platos': [{'Nombre': 'Milanesa con ensalada', 'Precio': 200},{'Nombre': 'Salteado de carne', 'Precio': 250}, {'Nombre': 'Guiso de mondongo', 'Precio': 320}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'SUSHI ADROGUE', 'Direccion': 'Int. Dr. Martín González 806, Adrogue, Buenos Aires', 'Telefono': '0810-220-2006', 'Posicion': (-34.798375, -58.396260), 'Radio de entrega': 0.5, 'Platos': [{'Nombre': 'Uramaki', 'Precio': 300},{'Nombre': 'Nirigi de atun', 'Precio': 350}, {'Nombre': 'Dorayakis', 'Precio': 400}], 'Total de ventas': 0, 'Moneda': 'ARG'}]
    return restaurantes

def cargar_clientes():
    clientes = [
        {'Nombre': 'LUCIA MARCHESANO', 'Contraseña': 'buonabitacolo31', 'Telefono': '011 4214-7576', 'Direccion': 'Erezcano 1576, Adrogue, Buenos aires', 'Posicion': (-34.802668, -58.375369), 'Rappicreditos': 0},
        {'Nombre': 'ANA MARIA GASPARUTTI', 'Contraseña': 'nuncioyana2019', 'Telefono': '011 4214-7576', 'Direccion': 'Av. Espora 200, Adrogué, Buenos aires', 'Posicion': (-34.788542, -58.389000), 'Rappicreditos': 0},
        {'Nombre': 'TERO MARTIGNETTI', 'Contraseña': 'onlyfood17', 'Telefono': '011 4293-6406', 'Direccion': 'King 725, José Mármol, Buenos aires', 'Posicion': (-34.789540, -58.373989), 'Rappicreditos': 0},
        {'Nombre': 'RAUL GARCIA', 'Contraseña': 'radiopasion1929', 'Telefono': '011 4293-1833', 'Direccion': 'Benigno Macias 443, Adrogue, Buenos aires', 'Posicion': (-34.797054, -58.391627), 'Rappicreditos': 0},
        {'Nombre': 'HORTENCIA CISTERNA', 'Contraseña': 'lamuniloca', 'Telefono': '011 4294-3936', 'Direccion': 'Cerretti 876, Adrogue, Buenos aires', 'Posicion': (-34.799099, -58.386906), 'Rappicreditos': 0}
        ]
    return clientes

def cargar_rappitenderos():
    rappitenderos = [
        {'Nombre': 'LUCIANA ARCOIRIS', 'Propina acumulada': 0, 'Posicion actual': (-34.789540, -58.373989), 'Pedido actual': None},
        {'Nombre': 'JONATHAN MOREL', 'Propina acumulada': 0, 'Posicion actual': (-34.797054, -58.391627), 'Pedido actual': None},
        {'Nombre': 'AURELIANO OLIVA', 'Propina acumulada': 0, 'Posicion actual': (-34.799099, -58.386906), 'Pedido actual': None},
        {'Nombre': 'ATENEA ANTI', 'Propina acumulada': 0, 'Posicion actual': (-34.788542, -58.389000), 'Pedido actual': None},
        {'Nombre': 'MORFI MOCHUELO', 'Propina acumulada': 0, 'Posicion actual': (-34.802668, -58.375369), 'Pedido actual': None}
    ]
    return rappitenderos

# Cargar 
def cargar_nuevo_restaurante(lista_restaurantes=[]):
    nombre = input(msg_nombre)
    while nombre!='*':
        if (nombre_no_existe_en_lista(nombre, lista_restaurantes) and nombre_tiene_formato_valido(nombre) and nombre_tiene_longitud_valida(nombre)):
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
            lista_restaurantes.append({'Nombre': nombre.upper(), 'Direccion': direccion, 'Telefono': telefono, 'Posicion': (float(latitud), float(longitud)), 'Radio de entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas': 0, 'Moneda': 'ARG'})            
        else:
            alertar_error("nombre", "\n a) Coincide con un plato existente en el restaurante. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    # print(lista_restaurantes)
    return lista_restaurantes   

def cargar_nuevo_plato():
    platos = []
    nombre = input(msg_nombre)
    while nombre!='*':
        if (nombre_no_existe_en_lista(nombre, platos) and nombre_tiene_formato_valido(nombre) and nombre_tiene_longitud_valida(nombre)):
            precio = input(msg_precio)
            while not precio_tiene_formato_valido(precio):
                alertar_error("precio", "\n a) No es un numero positivo. \n b) Tiene caracteres incorrectos para el indicio de decimal, utilice '.'. \n c) No se encuentra entre 0 y 9999.")           
                precio = input(msg_precio)
            platos.append({'Nombre': nombre.upper(), 'Precio': round(float(precio),2)})
        else:
            alertar_error("nombre", "\n a) Coincide con un plato existente en el restaurante. \n b) Tiene una longitud indebida (permitido entre 5 y 25 caracteres).")
        nombre = input(msg_nombre)
    # print(platos)
    return platos  

def cargar_nuevo_cliente():
