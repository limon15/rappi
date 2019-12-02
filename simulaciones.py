from prettytable import PrettyTable
from random import choice, randint, randrange
from common import validar_opcion_ingresada, evaluar_informacion_suficiente, imprimir_aviso_de_retorno_al_menu_anterior, imprimir_aviso_de_retorno_al_menu_anterior, pedir_variedad_max_platos, devolver_item_lista_entidad_segun_clave_valor
from math import radians, cos, sin, asin, sqrt

# Funcion que elige un valor al azar de una lista de diccionarios e imprime un breve detalle del valor obtenido en base a la clave proporcionada.
def obtener_valor_al_azar_de_lista_de_dic(lista, contenido, clave):
    random_choice = choice(lista)
    print("\n => El {} elegido al azar es: {}".format(contenido, random_choice[clave]))
    return random_choice

# Función que pide al usuario un número entre 1 y 100 (límite escogido por el grupo), evalúa
#si el dato ingresado es correcto y devuelve el número entero
def pedir_cantidad_simulaciones(valor_min=1, valor_max=100):
    opcion_valida = False
    while not opcion_valida:
        cantidad_simulaciones = input("Ingrese la cantidad de simulaciones que quiere realizar números (entre {} y {}): ".format(valor_min,valor_max))
        opcion_valida = validar_opcion_ingresada(cantidad_simulaciones, valor_max, valor_min)
    return int(cantidad_simulaciones)

def generar_lista_pedidos_aleatorios(lista_platos):
    lista_pedidos_aleatorios = []
    for i in range(len(lista_platos)):
        lista_pedidos_aleatorios.append((randint(1,10), lista_platos[i]['Nombre']))
    return lista_pedidos_aleatorios

def actualizar_item_lista_entidad(entidad, elem_anterior, elem_nuevo):
    entidad.remove(elem_anterior)
    entidad.append(elem_nuevo)
    return entidad
#------------------------------------------------------------------------------------------
# Funciones ya definidas en pedidos.py pero que no se pudieron importar por error.

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

def generar_reporte_pedido(pedido):
    t = PrettyTable(['CANT. PLATOS', 'PLATOS'])
    for i in range(len(pedido['Pedido'])):
        t.add_row([pedido['Pedido'][i][0], pedido['Pedido'][i][1]])
    print(t)

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

def mostrar_tiempo_estimado(distancia):
    velocidad_rappi = 15
    hora_estimada = distancia / velocidad_rappi
    minutos_estimados = hora_estimada * 60
    print(f"\n => El tiempo estimado de entrega será de {round(minutos_estimados,2)} minutos.") 
#----------------------------------------------------------------------------------

# Función encargarda de simular una cantidad n de pedidos. Actualizará los datos de
# usuarios, restaurantes y rappitenderos correspondientes. Al finalizar vuelve al menú principal.

def simulacion_de_pedidos(lista_clientes, lista_restaurantes, lista_rappitenderos):
    informacion_suficiente = evaluar_informacion_suficiente(lista_clientes, lista_restaurantes, lista_rappitenderos)
    if informacion_suficiente :
        cantidad_simulaciones = pedir_cantidad_simulaciones()
        variedad_max_platos = pedir_variedad_max_platos(1,10)
        i=0
        while i < cantidad_simulaciones:   
            print("\nSIMULACION {}".format(i))
            cliente_al_azar = obtener_valor_al_azar_de_lista_de_dic(lista_clientes, "cliente", "Nombre de usuario")
            lista_restaurantes_cercanos = devolver_entidad_cercana(cliente_al_azar, lista_restaurantes, 'Posicion', 'Posicion', 1)
            if len(lista_restaurantes_cercanos)!=0:
                restaurante_cercano = obtener_valor_al_azar_de_lista_de_dic(lista_restaurantes_cercanos, "restaurante", "Nombre") 
                variedad_platos = randint(1, len(restaurante_cercano['Platos'])) if variedad_max_platos>len(restaurante_cercano['Platos']) else randint(1,variedad_max_platos)
                print(f"\n => Se estableció una variedad de {variedad_platos} plato/s por pedido.\n")            
                lista_platos = restaurante_cercano['Platos'][:variedad_platos]
                lista_pedidos_aleatorios = generar_lista_pedidos_aleatorios(lista_platos)
                pedido = {'Pedido': lista_pedidos_aleatorios, 'Cliente': cliente_al_azar}
                generar_reporte_pedido(pedido)
                importe_total = obtener_importe_pedido_manual(lista_platos, lista_pedidos_aleatorios)
                print(f"\n => El importe total del pedido es de: ${importe_total}.")
                rappitendero_mas_cercano = devolver_entidad_cercana(restaurante_cercano, lista_rappitenderos, 'Posicion', 'Posicion actual', 2)
                print(f"\n => El rappitendero más cercano al restaurante es: {rappitendero_mas_cercano['Nombre']}")
                distancia_rappitendero_restaurante = calcular_distancia_terrestre(rappitendero_mas_cercano['Posicion actual'][0], rappitendero_mas_cercano['Posicion actual'][1], restaurante_cercano['Posicion'][0], restaurante_cercano['Posicion'][1])
                rappitendero_mas_cercano_actualizado = actualizar_distancia_recorrida_rappitendero(rappitendero_mas_cercano, distancia_rappitendero_restaurante)                
                distancia_restaurante_cliente = calcular_distancia_terrestre(restaurante_cercano['Posicion'][0], restaurante_cercano['Posicion'][1], cliente_al_azar['Posicion'][0], cliente_al_azar['Posicion'][1])
                rappitendero_mas_cercano_actualizado = actualizar_posicion_pedido_rappitendero(restaurante_cercano['Posicion'], pedido, rappitendero_mas_cercano_actualizado)
                rappitendero_mas_cercano_actualizado = actualizar_distancia_recorrida_rappitendero(rappitendero_mas_cercano, distancia_restaurante_cliente)
                distancia_total_recorrida = round(distancia_rappitendero_restaurante+distancia_restaurante_cliente,2)
                print(f"\n => El rappitendero recorrió una distancia total de: {distancia_total_recorrida} km.")
                mostrar_tiempo_estimado(distancia_total_recorrida)
                rappitendero_mas_cercano_actualizado = actualizar_posicion_pedido_rappitendero(cliente_al_azar['Posicion'], pedido, rappitendero_mas_cercano_actualizado)
                rappitendero_mas_cercano_actualizado, cliente_al_azar_actualizado = actualizar_ganancias_rappitendero_cliente(importe_total, rappitendero_mas_cercano_actualizado, cliente_al_azar)
                restaurante_mas_cercano_actualizado = actualizar_ventas_restaurante(importe_total, restaurante_cercano)
            else:
                print("No se encontraron restaurantes disponibles en la zona del cliente.")       
            i+=1
        lista_clientes = actualizar_item_lista_entidad(lista_clientes, cliente_al_azar, cliente_al_azar_actualizado)
        lista_restaurantes = actualizar_item_lista_entidad(lista_restaurantes, restaurante_cercano, restaurante_mas_cercano_actualizado)
        lista_rappitenderos = actualizar_item_lista_entidad(lista_rappitenderos, rappitendero_mas_cercano, rappitendero_mas_cercano_actualizado)
    imprimir_aviso_de_retorno_al_menu_anterior()    
    return lista_clientes, lista_restaurantes, lista_rappitenderos
      