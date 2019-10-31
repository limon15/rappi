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

# def solicitar_inicio_sesion():


# def pedido_manual():

# def validar_inicio_usuario(lista_clientes):
#     cliente = ''
#     while cliente == '':
#         nombre_usuario = input("Ingrese su nombre de usuario (no hay distincion de mayusculas): ").upper()
#         if not(no_existe_en_lista(nombre_usuario, 'Nombre de usuario', lista_clientes)) and usuario_tiene_formato_valido(nombre_usuario) and tiene_longitud_valida(nombre_usuario, 3, 12)):
#             cliente = devolver_item_lista_entidad_segun_clave_valor(lista_clientes, 'Nombre de usuario', nombre_usuario)
#         else:
#             alertar_error("usuario", "\n a) No coincide con un cliente existente. \n b) Tiene una longitud indebida (permitido entre 3 y 12 caracteres) \n c) Contiene espacios.")
#     nombre_usuario = input("Ingrese su nombre de usuario: ")            
#     return cliente        

# def iniciar_sesion(lista_clientes):    
#     validar_inicio_usuarios(lista_clientes)

#     usuario = input(msg_usuario) 


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