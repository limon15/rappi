from common import validar_opcion_ingresada
# Función que muestra los platos enumerados, con su precio, del restaurante elegido.
#Se muestra platos de la siguiente forma: 1,2...,n. Amentando en 1 la vista de la posición
#original del plato en la lista de platos.
def obtener_lista_de_platos(restaurant_elegido, limit=0):
    platos = []
    limit = len(restaurant_elegido['Platos']) if limit==0 else limit
    for i in range(limit):      
        platos.append(f"{restaurant_elegido['Platos'][i]['Nombre']} - ${restaurant_elegido['Platos'][i]['Precio']}")
    return platos

def calcular_importe_del_pedido(lista_platos, lista_pedidos):
    importe_total = 0
    for i in range(len(lista_platos)):
        for j in range(len(lista_pedidos)):
            if lista_pedidos[j][1] == lista_platos[i]['Nombre']:
                importe_unitario = lista_platos[i]['Precio']
                cantidad = lista_pedidos[j][0]
                importe_multiplicado = int(importe_unitario*cantidad)
        importe_total += importe_multiplicado
    return round(importe_total,2)
 
def actualizar_ganancias_rappitendero_cliente(importe_pedido, rappitendero, cliente):
    rappitendero['Propina acumulada'] += round(0.1*importe_pedido,2)
    if importe_pedido<200:
        cliente['Rappicreditos'] += round(0.1*importe_pedido,2)
    elif 200<importe_pedido<500: 
        cliente['Rappicreditos'] += round(0.15*importe_pedido,2)
    else: 
        cliente['Rappicreditos'] += round(0.2*importe_pedido,2)
    return rappitendero, cliente      

def actualizar_posicion_pedido_rappitendero(posicion_cliente, pedido, rappitendero):
    rappitendero['Posicion actual'] = posicion_cliente
    rappitendero['Pedido'] = pedido
    return rappitendero

def actualizar_ventas_restaurante(importe_pedido, restaurante):
    restaurante['Total de ventas'] += importe_pedido
    return restaurante

def pedir_variedad_max_platos(valor_min=1, valor_max=100):
    opcion_valida = False
    while not opcion_valida:
        variedad_max_platos = input("Ingrese la cantidad máxima de platos por pedido deseada: ")
        opcion_valida = validar_opcion_ingresada(variedad_max_platos, 100, 1)
    return int(variedad_max_platos)

    