from common import validar_opcion_ingresada, obtener_lista_nombres_restaurantes, devolver_opcion_elegida_validada_desde_lista, devolver_item_lista_entidad_segun_clave_valor, evaluar_existencia_entidad, imprimir_aviso_de_retorno_al_menu_anterior
from validaciones import no_existe_en_lista, alertar_error
from cargar_data import validar_nombre_eleccion_entidad, PrettyTable
from simulaciones import obtener_valor_al_azar_de_lista_de_dic, actualizar_item_lista_entidad
from math import radians, cos, sin, asin, sqrt

def actualizar_distancia_recorrida_rappitendero(rappitendero, distancia):
    rappitendero['Distancia recorrida']+= distancia
    return rappitendero


def calcular_distancia_terrestre(lon1, lat1, lon2, lat2):

    # Convierte grados decimales a radianes. Para esto importamos la librería math.
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Formula de Haversine
    # Fuente: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    radio = 6371 # Radio de la tierra en km.
    
    return c * radio

def devolver_entidad_cercana(entidad, lista_entidades, clave_entidad_1, clave_entidad_2, codigo):
    PROCESAR_RESTAURANTE = 1
    PROCESAR_RAPPITENDERO = 2
    lista_entidad_cercana = []
    lon1= entidad[clave_entidad_1][0]
    lat1= entidad[clave_entidad_1][1]
    distancia_minima = 1000 #variable exagerada pero que será reemplazada por el primero valor de distancia calculada para luego ir comparándose durante el bucle.

    for i in range(len(lista_entidades)):

        lon2 = lista_entidades[i][clave_entidad_2][0]
        lat2 = lista_entidades[i][clave_entidad_2][1]

        distancia_entre_entidades = calcular_distancia_terrestre(lon1, lat1, lon2, lat2)

        if codigo == PROCESAR_RESTAURANTE:
            if lista_entidades[i]['Radio de entrega'] > distancia_entre_entidades:
                lista_entidad_cercana.append(lista_entidades[i])

        elif codigo == PROCESAR_RAPPITENDERO:
            if distancia_entre_entidades < distancia_minima:
                distancia_minima = distancia_entre_entidades
                lista_entidad_cercana = lista_entidades[i]
    
    return lista_entidad_cercana

# Función que muestra los platos enumerados, con su precio, del restaurante elegido.
#Se muestra platos de la siguiente forma: 1,2...,n. Amentando en 1 la vista de la posición
#original del plato en la lista de platos.
def obtener_lista_de_platos(restaurant_elegido, limit=0):
    platos = []
    limit = len(restaurant_elegido['Platos']) if limit==0 else limit
    for i in range(limit):      
        platos.append(f"{restaurant_elegido['Platos'][i]['Nombre'].upper()} - ${restaurant_elegido['Platos'][i]['Precio']}")
    return platos

def obtener_importe_pedido_manual(lista_platos, lista_pedidos):
    importe_total = 0
    for i in range(len(lista_pedidos)):
        plato = devolver_item_lista_entidad_segun_clave_valor(lista_platos, 'Nombre', lista_pedidos[i][1])
        importe_total += float(plato['Precio'])*int(lista_pedidos[i][0])
    return importe_total

def actualizar_ganancias_rappitendero_cliente(importe_pedido, rappitendero, cliente):
    rappitendero['Propina acumulada'] += round(0.05*importe_pedido,2)
    if importe_pedido<200:
        cliente['Rappicreditos'] += round(0.05*importe_pedido,2)
    elif 200<importe_pedido<500: 
        cliente['Rappicreditos'] += round(0.10*importe_pedido,2)
    else: 
        cliente['Rappicreditos'] += round(0.15*importe_pedido,2)
    return rappitendero, cliente

def actualizar_posicion_pedido_rappitendero(posicion_nueva, pedido, rappitendero):
    rappitendero['Posicion actual'] = posicion_nueva
    rappitendero['Pedido'] = pedido
    return rappitendero

def actualizar_ventas_restaurante(importe_pedido, restaurante):
    restaurante['Total de ventas'] += importe_pedido
    return restaurante

def validar_nombre_usuario(lista_clientes):
    cliente = ''
    while cliente == '':
        nombre_usuario = input("Ingrese su nombre de usuario (no hay distincion de mayusculas): ").upper()
        if not (no_existe_en_lista(nombre_usuario, 'Nombre de usuario', lista_clientes)):
            cliente = devolver_item_lista_entidad_segun_clave_valor(lista_clientes, 'Nombre de usuario', nombre_usuario)
        else:
            alertar_error("usuario", "\n a) No coincide con un cliente existente.")
    return cliente 

def solicitar_cliente_valido(lista_clientes):
    cliente = ''
    while cliente == '':
        nombre_usuario = input("Ingrese su nombre de usuario (no hay distincion de mayúsculas/minúsculas): ").upper()
        if not (no_existe_en_lista(nombre_usuario, 'Nombre de usuario', lista_clientes)):
            cliente = devolver_item_lista_entidad_segun_clave_valor(lista_clientes, 'Nombre de usuario', nombre_usuario)
        else:
            alertar_error("usuario", "\n a) No coincide con un cliente existente.")
    return cliente 


def validar_contraseña(cliente):
    contraseña = input("Ingrese su contraseña: ")
    while contraseña != cliente['Contraseña']:
        alertar_error("contraseña", f"\n a) No coincide con la contrasaña almacenada para el usuario: {cliente['Nombre de usuario']}.")
        contraseña = input("Ingrese su contraseña: ")
    return True 


def iniciar_sesion_cliente(lista_clientes):
    cliente = solicitar_cliente_valido(lista_clientes)
    validar_contraseña(cliente)
    print("\n\t\tInicio exitoso.\n\t\t¡Hola {}!\n".format(cliente['Nombre de usuario']))
    return cliente 

def solicitar_cantidad_platos(nombre_plato, valor_min=1, valor_max=10):
    opcion_valida = False 
    while not opcion_valida:       
        cant_platos = input("Ingrese la cantidad de platos deseada para '{0}' (entre {1} y {2}): ".format(nombre_plato, valor_min, valor_max))
        opcion_valida = validar_opcion_ingresada(cant_platos, valor_max, valor_min)
    return int(cant_platos)

def continuar_pidiendo():
    continuar_pedido = input("¿Desea continuar pidiendo en el mismo restaurante? Ingrese 'si' o cualquier otro caracter para salir: ").upper()
    return True if continuar_pedido.upper() == 'SI' else False

def actualizar_pedido(lista_pedidos, cant_platos, nombre_plato):
    nombres_platos_pedidos = [n for (c, n) in lista_pedidos]
    if len(lista_pedidos) == 0 or nombre_plato not in nombres_platos_pedidos:
       lista_pedidos.append((cant_platos, nombre_plato))
    else:
        lista_pedidos = [(int(cant_platos)+int(c), nombre_plato) if (n == nombre_plato) else (c, n) for (c, n) in lista_pedidos]
    return lista_pedidos

# Función que recibe el origen y destino, para devolver la distancia que recorrerá el rappitendero.
def calcular_distancia(pos_restaurante, pos_cliente):
    a = (pos_restaurante[0] - pos_cliente[0] ) ** 2
    b = (pos_restaurante[1] - pos_cliente[1] ) ** 2
    distancia = 100 * ( (a + b) ** (1/2) )
    return distancia

# Función que solamente muestra en pantalla el tiempo estimado de entrega del pedido,
#siendo el origen del rappitendero en el restaurante hasta su destino.
def mostrar_tiempo_estimado(distancia):
    velocidad_rappi = 15
    hora_estimada = distancia / velocidad_rappi
    minutos_estimados = hora_estimada * 60
    print(f"\n => El tiempo estimado de entrega será de {round(minutos_estimados,2)} minutos.") 

def generar_reporte_pedido(pedido):
    t = PrettyTable(['CANT. PLATOS', 'PLATOS'])
    for i in range(len(pedido['Pedido'])):
        t.add_row([pedido['Pedido'][i][0], pedido['Pedido'][i][1]])
    print(t)

def elegir_restaurante(lista_restaurantes):
    eleccion_restaurante_valida = False
    while not eleccion_restaurante_valida:
        print("\nEstos son los restaurantes disponibles en tu zona:\n")
        nombres_restaurantes = obtener_lista_nombres_restaurantes(lista_restaurantes)
        indice_restaurante = devolver_opcion_elegida_validada_desde_lista(nombres_restaurantes, 2)
        eleccion_restaurante_valida = validar_nombre_eleccion_entidad(indice_restaurante, lista_restaurantes)
    restaurante = lista_restaurantes[indice_restaurante]
    return restaurante


def elegir_plato(restaurante):
    eleccion_platos_valida = False    
    while not eleccion_platos_valida:
        print("\nEstos son los platos disponibles del restaurante '{}':\n".format(restaurante['Nombre']))
        platos_restaurante = restaurante['Platos']
        lista_platos = obtener_lista_de_platos(restaurante)
        indice_plato = devolver_opcion_elegida_validada_desde_lista(lista_platos, 3)
        eleccion_platos_valida = validar_nombre_eleccion_entidad(indice_plato, platos_restaurante)
    nombre_plato =  platos_restaurante[indice_plato]['Nombre']
    return nombre_plato

def procesar_pedido_manual(pedido, cliente, restaurante, lista_clientes, lista_restaurantes, lista_rappitenderos, lista_rappitendero_mas_cercano):

    print("\nEste es su pedido:\n")
    generar_reporte_pedido(pedido)

    posicion_rappitendero = lista_rappitendero_mas_cercano['Posicion actual']
    posicion_restaurante = restaurante['Posicion']
    posicion_cliente = cliente['Posicion'] 

    distancia_rappitendero_restaurante = calcular_distancia_terrestre(posicion_rappitendero[0], posicion_rappitendero[1], posicion_restaurante[0], posicion_restaurante[1])

    rappitendero_mas_cercano_actualizado = actualizar_distancia_recorrida_rappitendero(lista_rappitendero_mas_cercano, distancia_rappitendero_restaurante) ## Actualizo la distancia recorrida desde donde estaba el rappitendero hacia el restaurante.
    rappitendero_mas_cercano_actualizado = actualizar_posicion_pedido_rappitendero(posicion_restaurante, pedido, rappitendero_mas_cercano_actualizado)
 
    print("\n => El pedido será entregado a la dirección: {}".format(cliente['Direccion']))      

    distancia_restaurante_cliente = calcular_distancia_terrestre(posicion_restaurante[0], posicion_restaurante[1], posicion_cliente[0], posicion_cliente[1])

    distancia_total_recorrida = round(distancia_rappitendero_restaurante,2)+round(distancia_restaurante_cliente,2)

    mostrar_tiempo_estimado(distancia_total_recorrida)
    rappitendero_mas_cercano_actualizado = actualizar_posicion_pedido_rappitendero(posicion_cliente, pedido, rappitendero_mas_cercano_actualizado)

    platos_restaurante = restaurante['Platos']
    importe_total = obtener_importe_pedido_manual(platos_restaurante, pedido['Pedido'])
    print("\n => El importe total a pagar es de: ${}.".format(importe_total))
    rappitendero_mas_cercano_actualizado, cliente_actualizado = actualizar_ganancias_rappitendero_cliente(importe_total, rappitendero_mas_cercano_actualizado, cliente)
    print("\n => El pedido ya fue recibido en su domicilio. Usted ganó {} rappicreditos por la compra.".format(cliente_actualizado['Rappicreditos']))
    
    rappitendero_mas_cercano_actualizado = actualizar_distancia_recorrida_rappitendero(rappitendero_mas_cercano_actualizado, distancia_restaurante_cliente) ## Actualizo la distancia recorrida desde donde estaba el rappitendero hacia el cliente.
    restaurante_actualizado = actualizar_ventas_restaurante(importe_total, restaurante) 

    lista_clientes = actualizar_item_lista_entidad(lista_clientes, cliente, cliente_actualizado)
    lista_restaurantes = actualizar_item_lista_entidad(lista_restaurantes, restaurante, restaurante_actualizado)
    lista_rappitenderos = actualizar_item_lista_entidad(lista_rappitenderos, lista_rappitendero_mas_cercano, rappitendero_mas_cercano_actualizado)

    print("\n Se cerrará su sesión.\n Hasta luego, vuelva pronto ☺.")
    return lista_clientes, lista_restaurantes, lista_rappitenderos


def pedido_manual(lista_clientes, lista_restaurantes, lista_rappitenderos):
    existen_clientes = evaluar_existencia_entidad(lista_clientes, 'clientes')
    if existen_clientes:
        cliente = iniciar_sesion_cliente(lista_clientes)
        existen_restaurantes = evaluar_existencia_entidad(lista_restaurantes, 'restaurantes')
        
        lista_restaurantes_cercanos = devolver_entidad_cercana(cliente, lista_restaurantes, 'Posicion', 'Posicion', 1) ## Agregué esta linea para obtener la lista de restaurantes cercanos.
        
        if (existen_restaurantes and len(lista_restaurantes_cercanos)!=0):
            continuar_pedido = True
            pedido = { 'Pedido': [], 'Cliente': cliente['Nombre de usuario'] }
            restaurante = elegir_restaurante(lista_restaurantes_cercanos)
            
            while continuar_pedido:
                nombre_plato = elegir_plato(restaurante)
                cant_plato = solicitar_cantidad_platos(nombre_plato, 1, 10)
                pedido['Pedido'] = actualizar_pedido(pedido['Pedido'], cant_plato, nombre_plato)
                continuar_pedido = continuar_pidiendo()

            lista_rappitendero_mas_cercano = devolver_entidad_cercana(restaurante, lista_rappitenderos, 'Posicion', 'Posicion actual', 2) ## Agregué esta linea para obtener la lista de datos del rappitendero mas cercano.
            lista_clientes, lista_rappitendero_mas_cercano, lista_rappitenderos = procesar_pedido_manual(pedido, cliente, restaurante, lista_clientes, lista_restaurantes, lista_rappitenderos, lista_rappitendero_mas_cercano) ## Agregué un parámetro (el de último lugar).
        else:
            print("Lo sentimos. No existen restaurantes disponibles en tu zona.")    

    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes, lista_restaurantes, lista_rappitenderos    