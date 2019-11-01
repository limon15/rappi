from common import validar_opcion_ingresada, obtener_lista_nombres_restaurantes, devolver_opcion_elegida_validada_desde_lista, devolver_item_lista_entidad_segun_clave_valor, evaluar_existencia_entidad, imprimir_aviso_de_retorno_al_menu_anterior
from validaciones import no_existe_en_lista, alertar_error
from cargar_data import validar_nombre_eleccion_entidad, PrettyTable, cargar_restaurantes_predefinidos
from simulaciones import obtener_valor_al_azar_de_lista_de_dic, actualizar_item_lista_entidad

# Función que muestra los platos enumerados, con su precio, del restaurante elegido.
#Se muestra platos de la siguiente forma: 1,2...,n. Amentando en 1 la vista de la posición
#original del plato en la lista de platos.
def obtener_lista_de_platos(restaurant_elegido, limit=0):
    platos = []
    limit = len(restaurant_elegido['Platos']) if limit==0 else limit
    for i in range(limit):      
        platos.append(f"{restaurant_elegido['Platos'][i]['Nombre']} - ${restaurant_elegido['Platos'][i]['Precio']}")
    return platos

# def calcular_importe_del_pedido(lista_platos, lista_pedidos):
#     importe_total = 0
#     for i in range(len(lista_platos)):
#         for j in range(len(lista_pedidos)):
#             if lista_pedidos[j][1] == lista_platos[i]['Nombre']:
#                 importe_unitario = lista_platos[i]['Precio']
#                 cantidad = lista_pedidos[j][0]
#                 importe_multiplicado = int(importe_unitario*cantidad)
#         importe_total += importe_multiplicado
#     return round(importe_total,2)

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

def generar_reporte(pedido):
    t = PrettyTable(['CANT. PLATOS', 'PLATOS'])
    for i in range(len(pedido['Pedido'])):
        t.add_row([pedido['Pedido'][i][0], pedido['Pedido'][i][1]])
    print(t)

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
    print("\n => El tiempo estimado de entrega será de {0:.2} minutos.\n".format(minutos_estimados))

def generar_reporte_pedido(pedido):
    t = PrettyTable(['CANT. PLATOS', 'PLATOS'])
    for i in range(len(pedido['Pedido'])):
        t.add_row([pedido['Pedido'][i][0], pedido['Pedido'][i][1]])
    print(t)

def pedido_manual(lista_clientes, lista_restaurantes, lista_rappitenderos):
    existen_clientes = evaluar_existencia_entidad(lista_clientes, 'clientes')
    if existen_clientes:
        cliente = iniciar_sesion_cliente(lista_clientes)
        eleccion_restaurante_valida = False
        continuar_pedido = True
        pedido = { 'Pedido': [], 'Cliente': cliente }
        while continuar_pedido:
            while not eleccion_restaurante_valida:
                print("\nEstos son los restaurantes disponibles en tu zona:\n")
                nombres_restaurantes = obtener_lista_nombres_restaurantes(lista_restaurantes)
                indice_restaurante = devolver_opcion_elegida_validada_desde_lista(nombres_restaurantes, 2)
                eleccion_restaurante_valida = validar_nombre_eleccion_entidad(indice_restaurante, lista_restaurantes)
            restaurante = lista_restaurantes[indice_restaurante]
            eleccion_platos_valida = False    
            while not eleccion_platos_valida:
                print("\nEstos son los platos disponibles del restaurante '{}':\n".format(restaurante['Nombre']))
                platos_restaurante = restaurante['Platos']
                lista_platos = obtener_lista_de_platos(restaurante)
                indice_plato = devolver_opcion_elegida_validada_desde_lista(lista_platos, 3)
                eleccion_platos_valida = validar_nombre_eleccion_entidad(indice_plato, platos_restaurante)
            nombre_plato =  platos_restaurante[indice_plato]['Nombre']
            cant_plato = solicitar_cantidad_platos(nombre_plato, 1, 10)
            pedido['Pedido'] = actualizar_pedido(pedido['Pedido'], cant_plato, nombre_plato)
            continuar_pedido = continuar_pidiendo()
        print("\nEste es su pedido:\n")
        generar_reporte_pedido(pedido)   
        rappitendero_al_azar = obtener_valor_al_azar_de_lista_de_dic(lista_rappitenderos, "rappitendero", "Nombre")
        posicion_restaurante = restaurante['Posicion']
        rappitendero_al_azar_actualizado = actualizar_posicion_pedido_rappitendero(posicion_restaurante, pedido, rappitendero_al_azar)
        posicion_cliente = cliente['Posicion']  
        print("\n => El pedido será entregado a la dirección: {}".format(cliente['Direccion']))      
        distancia = calcular_distancia(rappitendero_al_azar_actualizado['Posicion actual'], cliente['Posicion'])
        mostrar_tiempo_estimado(distancia)
        rappitendero_al_azar_actualizado = actualizar_posicion_pedido_rappitendero(posicion_cliente, pedido, rappitendero_al_azar_actualizado)
        importe_total = obtener_importe_pedido_manual(platos_restaurante, pedido['Pedido'])
        print("\n => El importe total a pagar es de: {}.".format(importe_total))
        rappitendero_al_azar_actualizado, cliente_actualizado = actualizar_ganancias_rappitendero_cliente(importe_total, rappitendero_al_azar_actualizado, cliente)
        print("\n => El pedido ya fue recibido en su domicilio. Usted ganó {} rappicreditos por la compra.".format(cliente_actualizado['Rappicreditos']))
        restaurante_actualizado = actualizar_ventas_restaurante(importe_total, restaurante) 
        lista_clientes = actualizar_item_lista_entidad(lista_clientes, cliente, cliente_actualizado)
        lista_restaurantes = actualizar_item_lista_entidad(lista_restaurantes, restaurante, restaurante_actualizado)
        lista_rappitenderos = actualizar_item_lista_entidad(lista_rappitenderos, rappitendero_al_azar, rappitendero_al_azar_actualizado)
        print("\n Se cerrará su sesión.\n Hasta luego, vuelva pronto ☺.")      
    imprimir_aviso_de_retorno_al_menu_anterior()
    return lista_clientes  