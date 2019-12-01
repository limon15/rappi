import pickle
from prettytable import PrettyTable

DATA_PRED = 'data_pred_'

def obtener_reporte_de_carga_predefinida(cant_inicial, cant_final, cant_fallados, entidad):
    t = PrettyTable(['CANT. INICIAL', 'CANT. FINAL', 'CANT. FALLADOS*'])
    t.add_row([cant_inicial, cant_final, cant_fallados])
    return print("REPORTE DE CARGA DE {}: \n{}{}\n".format(entidad.upper(), t, "\n* Se optó por no sobreescribir la data inicial" if cant_fallados>0 else ''))

def generar_archivos_pickle(lista_data_predefinida, nombre_entidad, nombre_adicional=''):
    file_name = '{nombre_adicional}{nombre_entidad}.pkl'.format(nombre_entidad = nombre_entidad, nombre_adicional=nombre_adicional)
    with open(file_name, 'wb') as pickle_file:
        pickle.dump(lista_data_predefinida, pickle_file)

def devolver_data_de_archivos_pickle(nombre_entidad, nombre_adicional=''):
    try:
        with open('{nombre_adicional}{nombre_entidad}.pkl'.format(nombre_entidad=nombre_entidad, nombre_adicional=nombre_adicional), 'rb') as pickle_file:
            data = pickle.load(pickle_file)
        return data
    except FileNotFoundError:
        return []        

def info_predefinida():
    restaurantes = [
        {'Nombre': 'MARIA BONITA', 'Direccion': 'Mitre 1195, Adrogue, Buenos Aires', 'Telefono': '011 4294-1184', 'Posicion': (-34.797054, -58.391627), 'Radio de entrega': 2.5, 'Platos': [{'Nombre': 'Ensalada Ninetta', 'Precio': 250},{'Nombre': 'Rissotto ai funghi', 'Precio': 370}, {'Nombre': 'Brotola a los 4 quesos', 'Precio': 570}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PASTA ROSSA', 'Direccion': 'Jorge San Pellerano 754, Adrogue, Buenos Aires', 'Telefono': '011 4214-3437', 'Posicion': (-34.799433, -58.390941), 'Radio de entrega': 1, 'Platos': [{'Nombre': 'Gnocchi souffle', 'Precio': 219},{'Nombre': 'Ravioli di formaggio', 'Precio': 229}, {'Nombre': 'Sorrentino di salmone', 'Precio': 310}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'PIZZERIA EL FARO', 'Direccion': 'Esteban Adrogué 1187, Adrogue, Buenos Aires', 'Telefono': '011 4214-4144', 'Posicion': (-34.798170, -58.390783), 'Radio de entrega': 3.5, 'Platos': [{'Nombre': 'Pizza muzzarella', 'Precio': 150},{'Nombre': 'Pizza napolitana', 'Precio': 170}, {'Nombre': 'Pizza ananá con azucar', 'Precio': 200}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'TIRIFILO EL BODEGON', 'Direccion': 'Cordero 694, Adrogue, Buenos Aires', 'Telefono': '011 4294-4195', 'Posicion': (-34.801080, -58.395488), 'Radio de entrega': 5, 'Platos': [{'Nombre': 'Milanesa con ensalada', 'Precio': 200},{'Nombre': 'Salteado de carne', 'Precio': 250}, {'Nombre': 'Guiso de mondongo', 'Precio': 320}], 'Total de ventas': 0, 'Moneda': 'ARG'},
        {'Nombre': 'SUSHI ADROGUE', 'Direccion': 'Int. Dr. Martín González 806, Adrogue, Buenos Aires', 'Telefono': '0810-220-2006', 'Posicion': (-34.798375, -58.396260), 'Radio de entrega': 0.5, 'Platos': [{'Nombre': 'Uramaki', 'Precio': 300},{'Nombre': 'Nirigi de atun', 'Precio': 350}, {'Nombre': 'Dorayakis', 'Precio': 400}], 'Total de ventas': 0, 'Moneda': 'ARG'}
        ]
    clientes = [
        {'Nombre de usuario': 'LUCHIA31', 'Contraseña': 'Buonabitacolo31!', 'Telefono': '011 4214-7576', 'Direccion': 'Erezcano 1576, Adrogue, Buenos aires', 'Posicion': (-34.802668, -58.375369), 'Rappicreditos': 0},
        {'Nombre de usuario': '2019AMARIAG', 'Contraseña': 'nuncioYana2019?', 'Telefono': '011 4214-7576', 'Direccion': 'Av. Espora 200, Adrogué, Buenos aires', 'Posicion': (-34.788542, -58.389000), 'Rappicreditos': 0},
        {'Nombre de usuario': 'BESTCATEVER', 'Contraseña': '#onlyFood17', 'Telefono': '011 4293-6406', 'Direccion': 'King 725, José Mármol, Buenos aires', 'Posicion': (-34.789540, -58.373989), 'Rappicreditos': 0},
        {'Nombre de usuario': 'RAULO1', 'Contraseña': 'Radiopa$ion1929', 'Telefono': '011 4293-1833', 'Direccion': 'Benigno Macias 443, Adrogue, Buenos aires', 'Posicion': (-34.797054, -58.391627), 'Rappicreditos': 0},
        {'Nombre de usuario': 'FLEQUI26', 'Contraseña': 'lamunil*CA1', 'Telefono': '011 4294-3936', 'Direccion': 'Cerretti 876, Adrogue, Buenos aires', 'Posicion': (-34.799099, -58.386906), 'Rappicreditos': 0}
    ]
    rappitenderos = [
        {'Nombre': 'LUCIANA ARCOIRIS', 'Propina acumulada': 0, 'Posicion actual': (-34.789540, -58.373989), 'Pedido actual': None, 'Distancia recorrida': 0},
        {'Nombre': 'JONATHAN MOREL', 'Propina acumulada': 0, 'Posicion actual': (-34.797054, -58.391627), 'Pedido actual': None, 'Distancia recorrida': 0},
        {'Nombre': 'AURELIANO OLIVA', 'Propina acumulada': 0, 'Posicion actual': (-34.799099, -58.386906), 'Pedido actual': None, 'Distancia recorrida': 0},
        {'Nombre': 'ATENEA ANTI', 'Propina acumulada': 0, 'Posicion actual': (-34.788542, -58.389000), 'Pedido actual': None, 'Distancia recorrida': 0},
        {'Nombre': 'MORFI MOCHUELO', 'Propina acumulada': 0, 'Posicion actual': (-34.802668, -58.375369), 'Pedido actual': None, 'Distancia recorrida': 0}
    ]
    generar_archivos_pickle(clientes, 'clientes', DATA_PRED)
    generar_archivos_pickle(restaurantes, 'restaurantes', DATA_PRED)
    generar_archivos_pickle(rappitenderos, 'rappitenderos', DATA_PRED)

def cargar_data_predefinida(lista_data, nombre_entidad):
    cant_inicial = len(lista_data)
    cant_fallados = 0
    # with open('{nombre_entidad}.pkl'.format(nombre_entidad=nombre_entidad), 'rb') as pickle_file:
    #     lista_data_predefinida = pickle.load(pickle_file)
    lista_data_predefinida = devolver_data_de_archivos_pickle(nombre_entidad, DATA_PRED)
    if cant_inicial != 0:   
        print("Ya existen {nombre_entidad} cargados\n¿Desea sobreescibirlos con la información predefinida?".format(nombre_entidad = nombre_entidad))
        confirmacion = input("Si acepta ingrese 'si', caso contrario ingrese cualquier caracteter: ")
        if confirmacion.upper() == 'SI':
            lista_data = lista_data_predefinida
            cant_final = len(lista_data)
        else:
            cant_fallados = len(lista_data_predefinida)
            cant_final = len(lista_data)
    else:
        lista_data = lista_data_predefinida
        cant_final = len(lista_data)
    obtener_reporte_de_carga_predefinida(cant_inicial, cant_final, cant_fallados, nombre_entidad)        
    return lista_data