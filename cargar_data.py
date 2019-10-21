def cargar_restaurantes():
    restaurantes = [
        {'Nombre': 'Maria Bonita', 'Direccion': 'Mitre 1195, Adrogue, Buenos Aires', 'Telefono': '011 4294-1184', 'Posicion': (-34.797054, -58.391627), 'Radio de entrega': 2.5, 'Platos': [{'Nombre': 'Ensalada Ninetta', 'Precio': 250},{'Nombre': 'Rissotto ai funghi', 'Precio': 370}, {'Nombre': 'Brotola a los 4 quesos', 'Precio': 570}], 'Total de ventas': None, 'Moneda': 'ARG'},
        {'Nombre': 'Pasta Rossa', 'Direccion': 'Jorge San Pellerano 754, Adrogue, Buenos Aires', 'Telefono': '011 4214-3437', 'Posicion': (-34.799433, -58.390941), 'Radio de entrega': 1, 'Platos': [{'Nombre': 'Gnocchi souffle', 'Precio': 219},{'Nombre': 'Ravioli di formaggio', 'Precio': 229}, {'Nombre': 'Sorrentino di salmone', 'Precio': 310}], 'Total de ventas': None, 'Moneda': 'ARG'},
        {'Nombre': 'Pizzeria el Faro', 'Direccion': 'Esteban Adrogué 1187, Adrogue, Buenos Aires', 'Telefono': '011 4214-4144', 'Posicion': (-34.798170, -58.390783), 'Radio de entrega': 3.5, 'Platos': [{'Nombre': 'Pizza muzzarella', 'Precio': 150},{'Nombre': 'Pizza napolitana', 'Precio': 170}, {'Nombre': 'Pizza ananá con azucar', 'Precio': 200}], 'Total de ventas': None, 'Moneda': 'ARG'},
        {'Nombre': 'Tirifilo El Bodegon', 'Direccion': 'Cordero 694, Adrogue, Buenos Aires', 'Telefono': '011 4294-4195', 'Posicion': (-34.801080, -58.395488), 'Radio de entrega': 5, 'Platos': [{'Nombre': 'Milanesa con ensalada', 'Precio': 200},{'Nombre': 'Salteado de carne', 'Precio': 250}, {'Nombre': 'Guiso de mondongo', 'Precio': 320}], 'Total de ventas': None, 'Moneda': 'ARG'},
        {'Nombre': 'Sushi Adrogue', 'Direccion': 'Int. Dr. Martín González 806, Adrogue, Buenos Aires', 'Telefono': '0810-220-2006', 'Posicion': (-34.798375, -58.396260), 'Radio de entrega': 0.5, 'Platos': [{'Nombre': 'Uramaki', 'Precio': 300},{'Nombre': 'Nirigi de atun', 'Precio': 350}, {'Nombre': 'Dorayakis', 'Precio': 400}], 'Total de ventas': None, 'Moneda': 'ARG'}]
    return restaurantes

def cargar_clientes():
    clientes = [
        {'Nombre': 'Lucia Marchesano', 'Contraseña': 'buonabitacolo31', 'Telefono': '011 4214-7576', 'Direccion': 'Erezcano 1576, Adrogue, Buenos aires', 'Posicion': (-34.802668, -58.375369), 'Rappicreditos': None},
        {'Nombre': 'Ana Maria Gasparutti', 'Contraseña': 'nuncioyana2019', 'Telefono': '011 4214-7576', 'Direccion': 'Av. Espora 200, Adrogué, Buenos aires', 'Posicion': (-34.788542, -58.389000), 'Rappicreditos': None},
        {'Nombre': 'Tero Martignetti', 'Contraseña': 'onlyfood17', 'Telefono': '011 4293-6406', 'Direccion': 'King 725, José Mármol, Buenos aires', 'Posicion': (-34.789540, -58.373989), 'Rappicreditos': None},
        # {'Nombre': 'Paola Rivera', 'Contraseña': '500elkilo', 'Telefono': '011 4294-1234', 'Direccion': 'Spiro 1075, Adrogue, Buenos aires', 'Posicion': (-34.799055, -58.391754), 'Rappicreditos': None},
        {'Nombre': 'Raul Garcia', 'Contraseña': 'radiopasion1929', 'Telefono': '011 4293-1833', 'Direccion': 'Benigno Macias 443, Adrogue, Buenos aires', 'Posicion': (-34.797054, -58.391627), 'Rappicreditos': None},
        {'Nombre': 'Hortencia Cisterna', 'Contraseña': 'lamuniloca', 'Telefono': '011 4294-3936', 'Direccion': 'Cerretti 876, Adrogue, Buenos aires', 'Posicion': (-34.799099, -58.386906), 'Rappicreditos': None}
        ]
    return clientes

def cargar_rappitenderos():
    rappitenderos = [
        {'Nombre': 'Luciana Arcoiris', 'Propina acumulada': None, 'Posicion actual': (-34.789540, -58.373989), 'Pedido actual': None},
        {'Nombre': 'Jonathan Morel', 'Propina acumulada': None, 'Posicion actual': (-34.797054, -58.391627), 'Pedido actual': None},
        {'Nombre': 'Aurelio Oliveri', 'Propina acumulada': None, 'Posicion actual': (-34.799099, -58.386906), 'Pedido actual': None},
        {'Nombre': 'Atenea Anti', 'Propina acumulada': None, 'Posicion actual': (-34.788542, -58.389000), 'Pedido actual': None},
        {'Nombre': 'Morfi Mochuelo', 'Propina acumulada': None, 'Posicion actual': (-34.802668, -58.375369), 'Pedido actual': None}
    ]
    return rappitenderos

restaurantes = cargar_restaurantes()
clientes = cargar_clientes()
rappitenderos = cargar_rappitenderos()

# print(len(restaurantes), restaurantes)
# def cargar_data_predefinida():


    # clientes = cargar_clientes()
    # rappitenderos = cargar_rappitenderos()

    # return restaurantes
    # , clientes, rappitenderos

# print(cargar_data_predefinida())
