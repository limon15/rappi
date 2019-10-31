from common import validar_opcion_ingresada, obtener_lista_nombres_restaurantes, devolver_opcion_elegida_validada_desde_lista, devolver_item_lista_entidad_segun_clave_valor, evaluar_existencia_entidad, imprimir_aviso_de_retorno_al_menu_anterior
from validaciones import no_existe_en_lista, alertar_error
from cargar_data import validar_nombre_eleccion_entidad
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
    contraseña_valida = validar_contraseña(cliente)
    print("\n\t\tInicio exitoso.\n\t\t¡Hola {}!\n".format(cliente['Nombre de usuario']))
    return cliente 

def solicitar_cantidad_platos(nombre_plato, valor_min=1, valor_max=10):
    opcion_valida = False 
    while not opcion_valida:       
        cant_platos = input("Ingrese la cantidad de platos deseada para '{0}' (entre {1} y {2}): ".format(nombre_plato, valor_min, valor_max))
        opcion_valida = validar_opcion_ingresada(cant_platos, valor_max, valor_min)
    return int(cant_platos)

def continuar_pidiendo():
    continuar_pedido = input("¿Desea continuar pidiendo? Ingrese 'si' o cualquier otro caracter para salir: ").upper()
    return True if continuar_pedido.upper() == 'SI' else False

def actualizar_pedido(lista_pedidos, cant_platos, nombre_plato):
    nombres_platos_pedidos = [n for (c, n) in lista_pedidos]
    if len(lista_pedidos) == 0 or nombre_plato not in nombres_platos_pedidos:
       lista_pedidos.append((cant_platos, nombre_plato))
    else:
        lista_pedidos = [(int(cant_platos)+int(c), nombre_plato) if (n == nombre_plato) else (c, n) for (c, n) in lista_pedidos]
    return lista_pedidos


def pedido_manual(lista_clientes, lista_restaurantes, lista_rappitenderos):
    existen_clientes = evaluar_existencia_entidad(lista_clientes, 'clientes')
    if existen_clientes:
        cliente = iniciar_sesion_cliente(lista_clientes)
        eleccion_restaurante_valida = False
        continuar_pedido = True
        pedidos = {'Pedido': [], 'Cliente': cliente }
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
                lista_platos = obtener_lista_de_platos(restaurante)
                # print(lista_platos)
                indice_plato = devolver_opcion_elegida_validada_desde_lista(lista_platos, 3)
                # print(indice_plato)
                eleccion_platos_valida = validar_nombre_eleccion_entidad(indice_plato, restaurante['Platos'])
            nombre_plato =  restaurante['Platos'][indice_plato]['Nombre']
            cant_plato = solicitar_cantidad_platos(nombre_plato, 1, 10)
            # pedido = (cant_plato, nombre_plato)
            # print(pedido)
            pedidos['Pedido'] = actualizar_pedido(pedidos['Pedido'], cant_plato, nombre_plato)
            print(pedidos)
            continuar_pedido = continuar_pidiendo()
    print(pedidos)     
    imprimir_aviso_de_retorno_al_menu_anterior()   


# pedido_manual()
#     while len(nombre_pedido) < 1 :
#         nombre_pedido = input("Nombre en blanco. Por favor ingrese un nombre: ")
        
#     return nombre_pedido   

#     usuario = input(msg_usuario)
#     while usuario!='*':



# def iniciar_sesion(dic_clientes):
    
#     nombre_ingresado = pedir_nombre()
#     nombre_encontrado = buscar_nombre(nombre_ingresado,dic_clientes)
    
#     if nombre_encontrado == "NO":
#         print("Nombre no encontrado. ")
#     seguir_pidiendo_nombre = "SI"
    
#     while (nombre_encontrado == "NO") and (seguir_pidiendo_nombre == "SI"):
#         nombre_ingresado = pedir_nombre()
#         nombre_encontrado = buscar_nombre(nombre_ingresado,dic_clientes)
#         if nombre_encontrado == "NO":
#             print("Nombre no encontrado. ")
#             seguir_pidiendo_nombre = desea_seguir("Desea seguir intentando ingresar el nombre?")
    
#     if nombre_encontrado == "SI":
#         contraseña_ingresada = pedir_contraseña()
#         contraseña_encontrada = buscar_contraseña(nombre_ingresado, contraseña_ingresada, dic_clientes)
#         if contraseña_encontrada == "NO":
#             print("Contraseña incorrecta. ")
            
#         seguir_pidiendo_contraseña = "SI"
        
#         while (contraseña_encontrada == "NO") and (seguir_pidiendo_contraseña == "SI"):
#             contraseña_ingresada = pedir_contraseña()
#             contraseña_encontrada = buscar_contraseña(nombre_ingresado, contraseña_ingresada, dic_clientes)
#             if contraseña_encontrada == "NO":
#                 seguir_pidiendo_contraseña = desea_seguir("Desea seguir intentando ingresar la contraseña?")
    
#     if nombre_encontrado == "SI" and contraseña_encontrada == "SI":
#         print(f"Te damos la bienvenida {nombre_ingresado}")
#         print("")
#         datos_usuario = devolver_datos_usuario(nombre_ingresado, contraseña_ingresada, dic_clientes)
        
#         return datos_usuario
    
#     else:
#         print("No se pudo iniciar sesión.")
    
#         return -1