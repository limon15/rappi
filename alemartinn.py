import random

def cargar_restaurantes():
    restaurantes = [
        {'Nombre': 'Maria Bonita', 'Direccion': 'Mitre 1195, Adrogue, Buenos Aires', 'Telefono': '011 4294-1184', 'Posicion': (-34.797054, -58.391627), 'Radio de entrega': 2.5, 'Platos': [{'Nombre': 'Ensalada Ninetta', 'Precio': 250},{'Nombre': 'Rissotto ai funghi', 'Precio': 370}, {'Nombre': 'Brotola a los 4 quesos', 'Precio': 570}], 'Total de ventas': 0.00, 'Moneda': 'ARG'},
        {'Nombre': 'Pasta Rossa', 'Direccion': 'Jorge San Pellerano 754, Adrogue, Buenos Aires', 'Telefono': '011 4214-3437', 'Posicion': (-34.799433, -58.390941), 'Radio de entrega': 1, 'Platos': [{'Nombre': 'Gnocchi souffle', 'Precio': 219},{'Nombre': 'Ravioli di formaggio', 'Precio': 229}, {'Nombre': 'Sorrentino di salmone', 'Precio': 310}], 'Total de ventas': 0.00, 'Moneda': 'ARG'},
        {'Nombre': 'Pizzeria el Faro', 'Direccion': 'Esteban Adrogué 1187, Adrogue, Buenos Aires', 'Telefono': '011 4214-4144', 'Posicion': (-34.798170, -58.390783), 'Radio de entrega': 3.5, 'Platos': [{'Nombre': 'Pizza muzzarella', 'Precio': 150},{'Nombre': 'Pizza napolitana', 'Precio': 170}, {'Nombre': 'Pizza ananá con azucar', 'Precio': 200}], 'Total de ventas': 0.00, 'Moneda': 'ARG'},
        {'Nombre': 'Tirifilo El Bodegon', 'Direccion': 'Cordero 694, Adrogue, Buenos Aires', 'Telefono': '011 4294-4195', 'Posicion': (-34.801080, -58.395488), 'Radio de entrega': 5, 'Platos': [{'Nombre': 'Milanesa con ensalada', 'Precio': 200},{'Nombre': 'Salteado de carne', 'Precio': 250}, {'Nombre': 'Guiso de mondongo', 'Precio': 320}], 'Total de ventas': 0.00, 'Moneda': 'ARG'},
        {'Nombre': 'Sushi Adrogue', 'Direccion': 'Int. Dr. Martín González 806, Adrogue, Buenos Aires', 'Telefono': '0810-220-2006', 'Posicion': (-34.798375, -58.396260), 'Radio de entrega': 0.5, 'Platos': [{'Nombre': 'Uramaki', 'Precio': 300},{'Nombre': 'Nirigi de atun', 'Precio': 350}, {'Nombre': 'Dorayakis', 'Precio': 400}], 'Total de ventas': 0.00, 'Moneda': 'ARG'}]
    return restaurantes

def cargar_clientes():
    clientes = [
        {'Nombre': 'Lucia Marchesano', 'Contraseña': 'buonabitacolo31', 'Telefono': '011 4214-7576', 'Direccion': 'Erezcano 1576, Adrogue, Buenos aires', 'Posicion': (-34.802668, -58.375369), 'Rappicreditos': 0.00},
        {'Nombre': 'Ana Maria Gasparutti', 'Contraseña': 'nuncioyana2019', 'Telefono': '011 4214-7576', 'Direccion': 'Av. Espora 200, Adrogué, Buenos aires', 'Posicion': (-34.788542, -58.389000), 'Rappicreditos': 0.00},
        {'Nombre': 'Tero Martignetti', 'Contraseña': 'onlyfood17', 'Telefono': '011 4293-6406', 'Direccion': 'King 725, José Mármol, Buenos aires', 'Posicion': (-34.789540, -58.373989), 'Rappicreditos': 0.00},
        {'Nombre': 'Raul Garcia', 'Contraseña': 'radiopasion1929', 'Telefono': '011 4293-1833', 'Direccion': 'Benigno Macias 443, Adrogue, Buenos aires', 'Posicion': (-34.797054, -58.391627), 'Rappicreditos': 0.00},
        {'Nombre': 'Hortencia Cisterna', 'Contraseña': 'lamuniloca', 'Telefono': '011 4294-3936', 'Direccion': 'Cerretti 876, Adrogue, Buenos aires', 'Posicion': (-34.799099, -58.386906), 'Rappicreditos': 0.00}
        ]
    return clientes

def cargar_rappitenderos():
    rappitenderos = [
        {'Nombre': 'Luciana Arcoiris', 'Propina acumulada': 0.00, 'Posicion actual': (-34.789540, -58.373989), 'Pedido actual': None},
        {'Nombre': 'Jonathan Morel', 'Propina acumulada': 0.00, 'Posicion actual': (-34.797054, -58.391627), 'Pedido actual': None},
        {'Nombre': 'Aurelio Oliveri', 'Propina acumulada': 0.00, 'Posicion actual': (-34.799099, -58.386906), 'Pedido actual': None},
        {'Nombre': 'Atenea Anti', 'Propina acumulada': 0.00, 'Posicion actual': (-34.788542, -58.389000), 'Pedido actual': None},
        {'Nombre': 'Morfi Mochuelo', 'Propina acumulada': 0.00, 'Posicion actual': (-34.802668, -58.375369), 'Pedido actual': None}
    ]
    return rappitenderos



def cerrar_rappi():
    print("Gracias por usar Rappi. ¡Hasta luego!")
    
# Función que solo muestra los restaurantes de mayor total de ventas ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_mejores_restaurantes_en_ventas(dic_restaurantes):
    dic_aux = sorted(dic_restaurantes, key = lambda x: x['Total de ventas'])
    dic_aux.reverse()
    i=0
    while i < len(dic_restaurantes) and i<10:
        print(f"El restaurante {dic_aux[i]['Nombre']} tiene $ {dic_aux[i]['Total de ventas']} como total de ventas.")
        i+=1
    
    print("Volviendo al submenú informes.")
    print("")
    

# Función que solo muestra los rappitenderos de mayor propina ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_rappitenderos_mayor_propina(dic_rappitenderos):
    dic_aux = sorted(dic_rappitenderos, key = lambda x: x['Propina acumulada'])
    dic_aux.reverse()
    i=0
    while i < len(dic_aux) and i<10:
        print(f"El rappitendero {dic_aux[i]['Nombre']} tiene $ {dic_aux[i]['Propina acumulada']} de propina acumulada.")
        i+=1
    
    print("Volviendo al submenú informes.")
    print("")
    
# Función que solo muestra los clientes de mayor rappicréditos ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_clientes_mayor_rappicreditos(dic_clientes):
    
    dic_aux = sorted(dic_clientes, key = lambda x: x['Rappicreditos'])
    dic_aux.reverse()

    i=0
    while i < len(dic_aux) and i<10:
        print(f"El cliente {dic_aux[i]['Nombre']} tiene {dic_aux[i]['Rappicreditos']} rappicréditos.")
        i+=1
    
    print("Volviendo al submenú informes.")
    print("")

# Función que solo muestra opciones, no pide ni devuelve ningun valor.
def mostrar_opciones_submenu_informes():
    print("Elija una opción para continuar: ")
    print("1. Clientes con mayor Rappicreditos.")
    print("2. Rappitenderos con mayor propina acumulada.")
    print("3. Restaurantes que mas ventas tuvieron.")
    print("4. Volver al menú principal.")

# Función que devuelve el número entero de la opción elegida del submenú informes.
def elegir_opcion_submenu_informes():
    
    CANTIDAD_OPCIONES_MAXIMA = 4
    mostrar_opciones_submenu_informes()
    opcion_elegida = input()
    opcion_valida = validar_opcion_ingresada(opcion_elegida, CANTIDAD_OPCIONES_MAXIMA)
    while opcion_valida == "NO":
        mostrar_opciones_submenu_informes()
        opcion_elegida = input()
        opcion_valida = validar_opcion_ingresada(opcion_elegida, CANTIDAD_OPCIONES_MAXIMA)
        
    print("")
    
    return int(opcion_elegida)


# Función encargada de mostrar algunas estadísticas de clientes, restaurantes y rappitenderos.
def informes(dic_clientes, dic_restaurantes, dic_rappitenderos):
    
    informacion_suficiente = evaluar_informacion_suficiente(dic_clientes, dic_restaurantes, dic_rappitenderos)
    
    if informacion_suficiente == "SI" :
    
        opcion_informes_elegida = elegir_opcion_submenu_informes()
        OPCION_VOLVER = 4
        
        while opcion_informes_elegida != OPCION_VOLVER :
            
            if opcion_informes_elegida == 1:
                mostrar_clientes_mayor_rappicreditos(dic_clientes)
                
            elif opcion_informes_elegida == 2:
                mostrar_rappitenderos_mayor_propina(dic_rappitenderos)
            
            elif opcion_informes_elegida == 3:
                mostrar_mejores_restaurantes_en_ventas(dic_restaurantes)
                
            opcion_informes_elegida = elegir_opcion_submenu_informes()

#-------------------------------------------------
        
# Función que elige un rappitendero al azar y devuelve un diccionario de sus datos.
def elegir_rappitendero_al_azar(dic_rappitendero):
    rappitendero_al_azar = random.choice(dic_rappitendero)
    print("El rappitendero elegido al azar es: {}".format(rappitendero_al_azar['Nombre']))
    
    return rappitendero_al_azar

# Función que devuelve un número al azar entre 1 y 10.
def cantidad_platos_al_azar():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    cantidad_platos_al_azar = random.choice(numeros)
    print("Elegiste al azar {} platos".format(cantidad_platos_al_azar))
    
    return cantidad_platos_al_azar

# Función que elige un restaurante al azar y devuelve un diccionario de sus datos.
def elegir_restaurante_al_azar(dicc_restaurantes):
    restaurante_al_azar = random.choice(dicc_restaurantes)
    print("El restaurante elegido al azar es: {}".format(restaurante_al_azar['Nombre']))
    return restaurante_al_azar


# Función que elige un cliente al azar y devuelve un diccionario de sus datos.
def elegir_cliente_al_azar(dicc_clientes):
    cliente_al_azar = random.choice(dicc_clientes)
    print("")
    print("El cliente elegido al azar es: {}".format(cliente_al_azar['Nombre']))
    return cliente_al_azar

# Función que pide al usuario un número entre 1 y 100 (límite escogido por el grupo), evalúa
#si el dato ingresado es correcto y devuelve el número entero
def pedir_cantidad_simulaciones():
    MINIMO_SIMULACIONES = 1
    MAXIMO_SIMULACIONES = 20

    cantidad_simulaciones = input("Ingrese cuantas simulaciones quiere hacer: ")
    opcion_valida = validar_opcion_ingresada(cantidad_simulaciones, MAXIMO_SIMULACIONES)
    while opcion_valida == "NO":
        cantidad_simulaciones = input("Ingrese números entre 1 y 20: ")
        opcion_valida = validar_opcion_ingresada(cantidad_simulaciones, MAXIMO_SIMULACIONES)
        
    return int(cantidad_simulaciones)


# Función encargarda de simular una cantidad n de pedidos. Actualizará los datos de
#usuarios, restaurantes y rappitenderos correspondientes. Al finalizar vuelve al menú principal.
def simulacion_de_pedidos(dicc_clientes, dicc_restaurantes, dicc_rappitenderos):
    
    informacion_suficiente = evaluar_informacion_suficiente(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)
    
    if informacion_suficiente == "SI":
        cantidad_simulaciones = pedir_cantidad_simulaciones()
        lista_pedidos_aleatorios = []
        IMPORTE_INICIAL = 0
        i=0
        while  i < cantidad_simulaciones:
            
            datos_usuario_elegido = elegir_cliente_al_azar(dicc_clientes)
            datos_restaurante_elegido = elegir_restaurante_al_azar(dicc_restaurantes)
            nombre_restaurante_elegido = datos_restaurante_elegido['Nombre']
            mostrar_platos(datos_restaurante_elegido)
        
            numero_plato_elegido = elegir_plato(datos_restaurante_elegido)
            plato_elegido = datos_restaurante_elegido['Platos'][numero_plato_elegido]['Nombre']
            precio_plato_elegido = datos_restaurante_elegido['Platos'][numero_plato_elegido]['Precio']
            cantidad_platos_elegidos = cantidad_platos_al_azar()
            lista_pedidos_aleatorios = [{'Restaurante': nombre_restaurante_elegido, 'Plato': plato_elegido, 'Cantidad': cantidad_platos_elegidos, 'Precio unidad': precio_plato_elegido}]
            
            datos_rappitendero_elegido = elegir_rappitendero_al_azar(dicc_rappitenderos)
            datos_rappitendero_elegido = actualizar_rappitendero(datos_rappitendero_elegido, datos_restaurante_elegido, lista_pedidos_aleatorios, IMPORTE_INICIAL)
            
            datos_rappitendero_elegido = actualizar_rappitendero(datos_rappitendero_elegido, datos_usuario_elegido['Posicion'], None, IMPORTE_INICIAL)
            importe_total = calcular_importe_del_pedido(lista_pedidos_aleatorios)
            
            actualizar_restaurante(datos_restaurante_elegido, importe_total)
            actualizar_cliente(datos_usuario_elegido, importe_total)
            actualizar_rappitendero(datos_rappitendero_elegido, datos_usuario_elegido['Posicion'], None, importe_total)
            #actualizar_propina_rappitendero(datos_rappitendero_elegido, importe_total)

            mostrar_actualizaciones_de_datos(datos_usuario_elegido, datos_restaurante_elegido, datos_rappitendero_elegido)
            
            i += 1
    
        print("Volviendo al menú principal")


#-------------------------------------------------

#Función que solamente muestra los cambios que se realizaron en los datos.
def mostrar_actualizaciones_de_datos(datos_usuario, datos_restaurante, datos_rappitendero):
    
    print("")
    print("ACTUALIZACIÓN CLIENTE")
    print(f"{datos_usuario['Nombre']} ahora tiene {datos_usuario['Rappicreditos']} rappicréditos.")
    print("")
    print("ACTUALIZACIÓN RESTAURANTE")
    print(f"{datos_restaurante['Nombre']} ahora tiene $ {datos_restaurante['Total de ventas']} como total de ventas.")
    print("")
    print("ACTUALIZACIÓN RAPPITENDERO")
    print(f"{datos_rappitendero['Nombre']} ahora tiene $ {datos_rappitendero['Propina acumulada']} de propina acumulada.")

    
# Función que actualiza el total de ventas del restaurante, no devuelve ningún valor.    
def actualizar_restaurante(datos_restaurante, importe_total):
    datos_restaurante['Total de ventas'] += importe_total

# Función que actualiza los rappicréditos del cliente.
def actualizar_cliente(datos_usuario, importe):
    
    if importe < 200:
        datos_usuario['Rappicreditos'] += 10 * importe / 100
    
    elif importe < 500:
        datos_usuario['Rappicreditos'] += 15 * importe / 100
    
    else:
        datos_usuario['Rappicreditos'] += 20 * importe / 100
        
    
# Función que recibe la lista de pedidos del usuario, calcula y devuele el precio total del pedido.
def calcular_importe_del_pedido(carrito):
    
    importe_total = 0
    acumulador = 0
    
    for i in range(len(carrito)):
        acumulador = carrito[i]['Precio unidad'] * carrito[i]['Cantidad']
        importe_total += acumulador
        
    #print(f"El importe total es ${importe_total} ")
    return importe_total


# Función que solamente muestra en pantalla el tiempo estimado de entrega del pedido,
#siendo el origen del rappitendero en el restaurante hasta su destino.
def mostrar_tiempo_estimado(distancia):
    
    velocidad_rappi = 15
    
    hora_estimada = distancia / velocidad_rappi
    minutos_estimados = hora_estimada * 60
    print("")
    print("El tiempo estimado de entrega será de {0:.2} minutos.".format(minutos_estimados))

# Función que recibe el origen y destino, para devolver la distancia que recorrerá el rappitendero.
def calcular_distancia(pos_restaurante, pos_cliente):
    
    a = (pos_restaurante[0] - pos_cliente[0] ) ** 2
    b = (pos_restaurante[1] - pos_cliente[1] ) ** 2
    distancia = 100 * ( (a + b) ** (1/2) )
    #print(f"La distancia es {distancia}")
    
    return distancia

# Función que asigna un origen, una lista de pedidos y la propina al rappitendero. Si el mismo ya entregó el
#pedido, entonces se le asignará un None. 
def actualizar_rappitendero(datos_rappitendero, origen_actual, lista_pedidos, importe):
    
    datos_rappitendero['Posicion actual'] = origen_actual
    datos_rappitendero['Pedido actual'] = lista_pedidos
    datos_rappitendero['Propina acumulada'] += 10 * importe/ 100
    
    return datos_rappitendero

# Función que devuelve los datos de un rappitendero seleccionado al azar.
def seleccionar_rappitendero(dicc_rapitenderos):
    
    #dicc_rapitenderos = cargar_rappitenderos()
    
    rappitendero_aleatorio = random.choice(dicc_rapitenderos)
    
    return rappitendero_aleatorio

# Función que verificará que el plato seleccionado por el usuario no haya sido
#elegido anteriormente. En caso de ser repetido, sumará las unidades del plato anterior
#con la actual.
def buscar_plato_repetido(lista_pedidos, plato_elegido, cantidad_platos):
    i=0
    encontro = "NO"
    while i < len(lista_pedidos) and encontro == "NO":
    
        if lista_pedidos[i]['Plato'] == plato_elegido:
            lista_pedidos[i]['Cantidad'] += cantidad_platos
            encontro = "SI"
            
        i+=1

    return encontro

# Función que recibe la opción ingresada, verifica si es un número y luego
#evalúa si el número está en el rango de opciones válidas mostradas en pantalla.
# Devuelve un string con SI en caso de ser una opcion válida, caso contrario devuelve NO.
def validar_opcion_ingresada(opcion, opcion_maxima):
    
    opcion_correcta = "NO"
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion > 0 and opcion <= opcion_maxima:
            opcion_correcta = "SI"
        else:
            print(f"Elija una opción valida.")
    else:
        print("El dato ingresado no es válido. Ingrese un número entero.")
        
    return opcion_correcta

# Función que pide al usuario ingresar una cantidad de platos para su pedido. Dentro se evalúa si
#la cantidad ingresada es válida, es decir, si se ingresó un número entre 1 y 10. Devuelve la
#cantidad ingresada.
def elegir_cantidad_platos():
    
    CANTIDAD_PLATOS_MAXIMO = 10
    unidades_plato = input("Ingrese las unidades que desea ordenar de este plato (mínimo 1 y máximo 10 incluidos): ")
    opcion_valida = validar_opcion_ingresada(unidades_plato, CANTIDAD_PLATOS_MAXIMO)
    while opcion_valida == "NO":
        unidades_plato = input("Ingrese las unidades que desea ordenar de este plato (mínimo 1 y máximo 10 incluidos): ")
        opcion_valida = validar_opcion_ingresada(unidades_plato, CANTIDAD_PLATOS_MAXIMO)
    
    return int(unidades_plato)

# Función que pide al usuario elegir un plato del restaurante. Se evalúa que el dato
#sea válido (número entero entre 1 y la número máximo de variedad de platos del restaurante.
#Devuelve un número entero - 1 porque es la posición original del plato en la lista de platos.
def elegir_plato(restaurant_elegido):
    
    NUMEROS_PLATOS_MAXIMO = len(restaurant_elegido['Platos'])
    
    n_plato_elegido = input("Elija un plato: ")
    opcion_valida = validar_opcion_ingresada(n_plato_elegido, NUMEROS_PLATOS_MAXIMO)
    while opcion_valida == "NO":
        n_plato_elegido = input("Elija un plato: ")
        opcion_valida = validar_opcion_ingresada(n_plato_elegido, NUMEROS_PLATOS_MAXIMO)
    
    return (int(n_plato_elegido) - 1)

# Función que muestra los platos enumerados, con su precio, del restaurante elegido.
#Se muestra platos de la siguiente forma: 1,2...,n. Amentando en 1 la vista de la posición
#original del plato en la lista de platos.
def mostrar_platos(restaurant_elegido):
    print("---------------------------")
    print("   PLATOS       ")
    for i in range(len(restaurant_elegido['Platos'])):      
        print(f"{i+1}. {restaurant_elegido['Platos'][i]['Nombre']} - ${restaurant_elegido['Platos'][i]['Precio']} ")
    
    print("")
        
# Función que pide al usuario elegir un restaurante. Se evalúa que el dato
#sea válido (número entero entre 1 y la cantidad de restaurantes existentes).
#Devuelve un número entero - 1 porque es la posición original del restaurante en la lista de diccionarios.
def elegir_restaurante(dic_restaurantes):
    
    NUMEROS_RESTAURANTES_MAXIMO = len(dic_restaurantes)
    
    n_restaurante_elegido = input("Elija un restaurante: ")
    opcion_valida = validar_opcion_ingresada(n_restaurante_elegido, NUMEROS_RESTAURANTES_MAXIMO)
    while opcion_valida == "NO":
        n_restaurante_elegido = input("Elija un restaurante: ")
        opcion_valida = validar_opcion_ingresada(n_restaurante_elegido, NUMEROS_RESTAURANTES_MAXIMO)
    
    n_restaurante_elegido = int(n_restaurante_elegido)
    
    return dic_restaurantes[n_restaurante_elegido - 1]

# Función que muestra los restaurantes enumerados de la siguiente forma: 1,2...,n.
#Amentando en 1 la vista de la posición original del restaurante en la lista de diccionarios.
def mostrar_restaurantes(dic_restaurantes):
    print("---------------------------")
    print("   RESTAURANTES       ")
    for i in range(len(dic_restaurantes)):
        print(f"{i+1}. {dic_restaurantes[i]['Nombre']} - {dic_restaurantes[i]['Direccion']} - {dic_restaurantes[i]['Telefono']}.")
    print("")

# Función que devuelve la biblioteca con todos los datos del usuario que inició sesión.
def devolver_datos_usuario(nombre_ingresado, contraseña_ingresada, dic_clientes):
    
    pos = 0
    encontro = "NO"
    
    while encontro == "NO" and pos < len(dic_clientes):
        if dic_clientes[pos]['Nombre'] == nombre_ingresado and dic_clientes[pos]['Contraseña'] == contraseña_ingresada:
            encontro = "SI"
        if encontro == "NO":
            pos+=1
        
    return dic_clientes[pos]

# Función que pregunta al usuario si desea seguir ejecutando algún bucle externo con su
#mensaje correspondiente. En caso de ingresar 1, devolverá SI,
#en caso de ingresar 2, devolverá NO.
def desea_seguir(mensaje):
    
    OPCION_MAXIMA = 2
    print(mensaje)
    print("1. Si")
    print("2. No")
    opcion_elegida = input()
    opcion_valida = validar_opcion_ingresada(opcion_elegida, OPCION_MAXIMA) #
    
    while opcion_valida == "NO":
        print(mensaje)
        print("1. Si")
        print("2. No")
        opcion_elegida = input()
        opcion_valida = validar_opcion_ingresada(opcion_elegida, OPCION_MAXIMA)
        
    opcion_elegida = int(opcion_elegida)
    
    if opcion_elegida == 1:
        seguir = "SI"
    elif opcion_elegida == 2:
        seguir ="NO"
        
    return seguir

# Función que busca la contraseña ingresada del usuario en los diccionarios.
#Devuelve SI en caso de encontrar la contraseña y NO en caso contrario.
def buscar_contraseña(nombre_ingresado, contraseña_ingresada, dic_clientes):
    
    encontro_contraseña = "NO"
    i = 0
    while encontro_contraseña == "NO" and i < len(dic_clientes):
        if dic_clientes[i]['Nombre'] == nombre_ingresado and dic_clientes[i]['Contraseña'] == contraseña_ingresada:
            encontro_contraseña = "SI"
        i+=1
        
    return encontro_contraseña
    
#5.1.d. Función que pide al usuario una contraseña, el bucle impedirá que se ingrese
#una cadena vacía. Devuelve la cadena ingresada.
def pedir_contraseña():
    contraseña_pedida = input("Ingrese una contraseña: ")
    while len(contraseña_pedida) < 1 :
        contraseña_pedida = input("contraseña en blanco. Por favor ingrese una contraseña: ")
        
    return contraseña_pedida  

# Función que busca el nombre del usuario en los diccionarios.
#Devuelve SI en caso de encontrar la contraseña y NO en caso contrario.
def buscar_nombre(nombre_ingresado, dic_clientes):
    
    i=0
    encontro_nombre = "NO"
    while (encontro_nombre == "NO") and (i < len(dic_clientes)):
        if dic_clientes[i]['Nombre'] == nombre_ingresado:
            encontro_nombre = "SI"
        i+=1
    
    return encontro_nombre

# Función que pide al usuario un nombre. El bucle impedirá que se ingrese
#una cadena vacía. Devuelve la cadena ingresada.
def pedir_nombre():
    
    nombre_pedido = input("Ingrese un nombre: ")
    while len(nombre_pedido) < 1 :
        nombre_pedido = input("Nombre en blanco. Por favor ingrese un nombre: ")
        
    return nombre_pedido    
    
# Función que se encarga de iniciar sesión con éxito o devolver -1 en caso de que
#el usuario no haya podido ingresar sesión.
def iniciar_sesion(dic_clientes):
    
    nombre_ingresado = pedir_nombre()
    nombre_encontrado = buscar_nombre(nombre_ingresado,dic_clientes)
    
    if nombre_encontrado == "NO":
        print("Nombre no encontrado. ")
    seguir_pidiendo_nombre = "SI"
    
    while (nombre_encontrado == "NO") and (seguir_pidiendo_nombre == "SI"):
        nombre_ingresado = pedir_nombre()
        nombre_encontrado = buscar_nombre(nombre_ingresado,dic_clientes)
        if nombre_encontrado == "NO":
            print("Nombre no encontrado. ")
            seguir_pidiendo_nombre = desea_seguir("Desea seguir intentando ingresar el nombre?")
    
    if nombre_encontrado == "SI":
        contraseña_ingresada = pedir_contraseña()
        contraseña_encontrada = buscar_contraseña(nombre_ingresado, contraseña_ingresada, dic_clientes)
        if contraseña_encontrada == "NO":
            print("Contraseña incorrecta. ")
            
        seguir_pidiendo_contraseña = "SI"
        
        while (contraseña_encontrada == "NO") and (seguir_pidiendo_contraseña == "SI"):
            contraseña_ingresada = pedir_contraseña()
            contraseña_encontrada = buscar_contraseña(nombre_ingresado, contraseña_ingresada, dic_clientes)
            if contraseña_encontrada == "NO":
                seguir_pidiendo_contraseña = desea_seguir("Desea seguir intentando ingresar la contraseña?")
    
    if nombre_encontrado == "SI" and contraseña_encontrada == "SI":
        print(f"Te damos la bienvenida {nombre_ingresado}")
        print("")
        datos_usuario = devolver_datos_usuario(nombre_ingresado, contraseña_ingresada, dic_clientes)
        
        return datos_usuario
    
    else:
        print("No se pudo iniciar sesión.")
    
        return -1
    
    
# Función que recibe 3 diccionarios, evalúa si tienen información dentro, en caso de que los 3 estén cargados
#va a devolver que la información suficiente es "SI", en caso de que algún diccionario esté vacío, devolverá que
#la información suficiente es "NO".
def evaluar_informacion_suficiente(dicc_clientes, dicc_restaurantes, dicc_rappitenderos):
    
    info_suficiente = "SI"
    
    if len(dicc_clientes) == 0 or len(dicc_restaurantes) == 0 or len(dicc_rappitenderos) == 0:
        info_suficiente = "NO"
        print("No hay suficiente información para ejecutar esta opción, pruebe cargando datos de clientes, restaurantes y rappitenderos previamente.")
        print("Volviendo al menú principal.")
    
    return info_suficiente

# Función que ejecuta el pedido de un usuario que inició sesión con éxito.
# Al finalizar, los datos del cliente, restaurante y rappitendero serán actualizados.
def pedido_manual(dicc_clientes, dicc_restaurantes, dicc_rappitenderos):
    
    informacion_suficiente = evaluar_informacion_suficiente(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)
    
    if informacion_suficiente == "SI":
        
        print("----------------------------------------------")
        print("Pedido manual.")
        
        datos_usuario = iniciar_sesion(dicc_clientes)
    
        if datos_usuario == -1 :
            print("Volviendo al menú principal.")
        else:
            
            lista_pedidos = [] #Lista vacía que contendrá el restaurante, plato y unidades elegidas.
            IMPORTE_INICIAL = 0 
            
            mostrar_restaurantes(dicc_restaurantes)
            
            datos_restaurante = elegir_restaurante(dicc_restaurantes)
            nombre_restaurante_elegido = datos_restaurante['Nombre']
            posicion_restaurante_elegido = datos_restaurante['Posicion'] 
            
            mostrar_platos(datos_restaurante)
            
            num_plato_elegido = elegir_plato(datos_restaurante)
            plato_elegido = datos_restaurante['Platos'][num_plato_elegido]['Nombre']
            precio_plato_elegido = datos_restaurante['Platos'][num_plato_elegido]['Precio']
            cantidad_platos = elegir_cantidad_platos()

            lista_pedidos.append({'Restaurante': nombre_restaurante_elegido, 'Plato': plato_elegido, 'Cantidad': cantidad_platos, 'Precio unidad': precio_plato_elegido})
            
            seguir_realizando_pedidos = desea_seguir("Desea seguir realizando pedidos en el mismo restaurante?")
            
            while seguir_realizando_pedidos == "SI" :
                
                mostrar_platos(datos_restaurante)
                
                num_plato_elegido = elegir_plato(datos_restaurante)
                plato_elegido = datos_restaurante['Platos'][num_plato_elegido]['Nombre']
                precio_plato_elegido = datos_restaurante['Platos'][num_plato_elegido]['Precio']
                cantidad_platos = elegir_cantidad_platos()
                encontro_plato_repetido = buscar_plato_repetido(lista_pedidos, plato_elegido, cantidad_platos)
                    
                if encontro_plato_repetido == "NO":
                    lista_pedidos.append({'Restaurante': nombre_restaurante_elegido, 'Plato': plato_elegido, 'Cantidad': cantidad_platos, 'Precio unidad': precio_plato_elegido})
                
                seguir_realizando_pedidos = desea_seguir("Desea seguir realizando pedidos en el mismo restaurante?")
                print("")
                
            for i in range(len(lista_pedidos)): #Este bucle solo muestra la lista de pedidos.
                print(lista_pedidos[i]) 
            print("Su pedido será asignado a un rappitendero.")

            datos_rappitendero = seleccionar_rappitendero(dicc_rappitenderos)
            datos_rappitendero = actualizar_rappitendero(datos_rappitendero, posicion_restaurante_elegido, lista_pedidos, IMPORTE_INICIAL)
            
            distancia = calcular_distancia(datos_rappitendero['Posicion actual'], datos_usuario['Posicion'])
            mostrar_tiempo_estimado(distancia)
            
            datos_rappitendero = actualizar_rappitendero(datos_rappitendero, datos_usuario['Posicion'], None, IMPORTE_INICIAL)
            importe_total = calcular_importe_del_pedido(lista_pedidos)
            
            actualizar_restaurante(datos_restaurante, importe_total)
            actualizar_cliente(datos_usuario, importe_total)
            actualizar_rappitendero(datos_rappitendero, datos_usuario['Posicion'], None, importe_total)
            
            mostrar_actualizaciones_de_datos(datos_usuario, datos_restaurante, datos_rappitendero)
            
            print("Volviendo al menú principal")
        
#------------------------------------------------------------
        
# Parte 2 del tp
def carga_informacion_manual():
    print("Carga de información manual.")
    print("Volviendo al menú principal.")

#------------------------------------------------------

# Función que recibe información predefinida de cliente, restaurante o rappitendero y los muestra
#en pantalla.
def mostrar_informacion_predefinida(dicc_info_predefinida, mensaje):
    
    print(mensaje)
    for i in range(len(dicc_info_predefinida)):
        print(dicc_info_predefinida[i])
    print("")

# Función encargada de cargar la información predefinida en las listas de diccionarios de clientes,
#restaurantes y rappitenderos. En caso de haber cargado previamente esta información, muestra un
#mensaje en pantalla informando que la acción no se puede realizar por segunda vez.
def carga_informacion_predefinida(dicc_clientes, dicc_restaurantes, dicc_rappitenderos):
    
    if len(dicc_clientes) != 0 :
        info_predef_clientes = cargar_clientes()
        
        if info_predef_clientes != dicc_clientes:
            dicc_clientes.append(info_predef_clientes)
        else:
            print("Ya cargaste esta información de clientes.")
    
    else:
        dicc_clientes = cargar_clientes()
        mostrar_informacion_predefinida(dicc_clientes, "INFORMACIÓN DE CLIENTES PREDEFINIDOS CARGADA CON ÉXITO.")
    
    
    if len(dicc_restaurantes) != 0 :
        info_predef_restaurantes = cargar_restaurantes()
        
        if info_predef_restaurantes != dicc_restaurantes:
            dicc_restaurantes.append(info_predef_restaurantes)
        else:
            print("Ya cargaste esta información de restaurantes.")
        
    else:
        dicc_restaurantes = cargar_restaurantes()
        mostrar_informacion_predefinida(dicc_restaurantes, "INFORMACIÓN DE RESTAURANTES PREDEFINIDOS CARGADA CON ÉXITO.")
    
    
    if len(dicc_rappitenderos) != 0 :
        info_predef_rappitenderos = cargar_rappitenderos()
        
        if info_predef_rappitenderos != dicc_rappitenderos:
            dicc_rappitenderos.append(info_predef_rappitenderos)
        else:
            print("Ya cargaste esta información de rappitenderos.")
        
    else:
        dicc_rappitenderos = cargar_rappitenderos()
        mostrar_informacion_predefinida(dicc_rappitenderos, "INFORMACIÓN DE RAPPITENDEROS PREDEFINIDOS CARGADA CON ÉXITO.")
    
    
    return dicc_clientes, dicc_restaurantes, dicc_rappitenderos
    
# Función que solamente muestra las opciones del menú principal, sin recibir ni devolver datos.
def mostrar_opciones_menu_principal():
    print("")
    print("Elija una opción para continuar: ")
    print("1. Carga de información predefinida.")
    print("2. Carga de información manual.")
    print("3. Pedido manual.")
    print("4. Simulación de pedidos.")
    print("5. Informes.")
    print("6. Salir.")
    
# Función que pide al usuario una opción válida para ejecutar la acción correspondiente.
#Recibe un caracter, evalúa que sea un número entero entre 1 y 6 (opciones válidas), y lo devuelve.
def elegir_opcion_menu_principal():
    
    CANTIDAD_OPCIONES_MAXIMA = 6
    mostrar_opciones_menu_principal()
    opcion_elegida = input()
    opcion_valida = validar_opcion_ingresada(opcion_elegida, CANTIDAD_OPCIONES_MAXIMA)
    while opcion_valida == "NO":
        mostrar_opciones_menu_principal()
        opcion_elegida = input()
        opcion_valida = validar_opcion_ingresada(opcion_elegida, CANTIDAD_OPCIONES_MAXIMA)
        
    print("")
    
    return int(opcion_elegida)
    
# Función encargada de ejecutar todas las acciones del programa tantas veces sea requerido.
#Se espera que el usuario seleccione primero la opción 1 o 2 para realizar 
def iniciar_rappi():
    
    print("Bienvenido a Rappi !")
    
    dicc_clientes = []
    dicc_restaurantes = []
    dicc_rappitenderos = []
    
    opcion_elegida = elegir_opcion_menu_principal()
    OPCION_SALIR = 6
    
    while opcion_elegida != OPCION_SALIR :
    
        if opcion_elegida == 1:
            dicc_clientes, dicc_restaurantes, dicc_rappitenderos = carga_informacion_predefinida(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)
        
        elif opcion_elegida == 2:
            carga_informacion_manual()
        
        elif opcion_elegida == 3:
            pedido_manual(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)
        
        elif opcion_elegida == 4:
            simulacion_de_pedidos(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)
        
        elif opcion_elegida == 5:
            informes(dicc_clientes, dicc_restaurantes, dicc_rappitenderos)

        opcion_elegida = elegir_opcion_menu_principal()


# Función principal donde se ejecuta rappi.
def main():
    
    iniciar_rappi()
    cerrar_rappi()
    
main()