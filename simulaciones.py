from prettytable import PrettyTable
# from pedidos import obtener_importe_pedido_manual, actualizar_posicion_pedido_rappitendero, actualizar_ganancias_rappitendero_cliente, actualizar_ventas_restaurante, pedir_variedad_max_platos
from random import choice, randint, randrange
from common import validar_opcion_ingresada, evaluar_informacion_suficiente, imprimir_aviso_de_retorno_al_menu_anterior, imprimir_aviso_de_retorno_al_menu_anterior, pedir_variedad_max_platos, devolver_item_lista_entidad_segun_clave_valor
# from pedidos import *

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
        cantidad_simulaciones = input("Ingrese la cantidad de simulaciones que quiere realizar números entre {} y {}: ".format(valor_min,valor_max))
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
    rappitendero['Propina acumulada'] += round(0.1*importe_pedido,2)
    if importe_pedido<200:
        cliente['Rappicreditos'] += round(0.1*importe_pedido,2)
    elif 200<importe_pedido<500: 
        cliente['Rappicreditos'] += round(0.15*importe_pedido,2)
    else: 
        cliente['Rappicreditos'] += round(0.2*importe_pedido,2)
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
            restaurante_al_azar = obtener_valor_al_azar_de_lista_de_dic(lista_restaurantes, "restaurante", "Nombre")
            variedad_platos = randint(1, len(restaurante_al_azar['Platos'])) if variedad_max_platos>len(restaurante_al_azar['Platos']) else randint(1,variedad_max_platos)
            print(f"\n => Se estableció una variedad de {variedad_platos} plato/s por pedido.\n")            
            lista_platos = restaurante_al_azar['Platos'][:variedad_platos]
            lista_pedidos_aleatorios = generar_lista_pedidos_aleatorios(lista_platos)
            pedido = {'Pedido': lista_pedidos_aleatorios, 'Cliente': cliente_al_azar}
            generar_reporte_pedido(pedido)
            importe_total = obtener_importe_pedido_manual(lista_platos, lista_pedidos_aleatorios)
            print("\n => El importe total del pedido es de: {}.".format(importe_total))
            rappitendero_al_azar = obtener_valor_al_azar_de_lista_de_dic(lista_rappitenderos, "rappitendero", "Nombre")
            posicion_cliente = cliente_al_azar['Posicion']
            rappitendero_al_azar_actualizado = actualizar_posicion_pedido_rappitendero(posicion_cliente, pedido, rappitendero_al_azar)
            rappitendero_al_azar_actualizado, cliente_al_azar_actualizado = actualizar_ganancias_rappitendero_cliente(importe_total, rappitendero_al_azar, cliente_al_azar)
            restaurante_al_azar_actualizado = actualizar_ventas_restaurante(importe_total, restaurante_al_azar)
            i+=1
        lista_clientes = actualizar_item_lista_entidad(lista_clientes, cliente_al_azar, cliente_al_azar_actualizado)
        lista_restaurantes = actualizar_item_lista_entidad(lista_restaurantes, restaurante_al_azar, restaurante_al_azar_actualizado)
        lista_rappitenderos = actualizar_item_lista_entidad(lista_rappitenderos, rappitendero_al_azar, rappitendero_al_azar_actualizado)
    imprimir_aviso_de_retorno_al_menu_anterior()    
    return lista_clientes, lista_restaurantes, lista_rappitenderos
      