# msg_eleccion = "La eleccion elegida fue: {}. Si es correcto escriba 'si' de lo contrario escriba 'no': ".format(restaurantes[eleccion]['Nombre'])
from prettytable import PrettyTable

def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero referido a las opciones del menu: "))
            correcto = True
        except ValueError:
            print('Error. La opcion ingresada no es un numero entero.')
    return num

# Función que recibe 3 diccionarios, evalúa si tienen información dentro, en caso de que los 3 estén cargados
#va a devolver que la información suficiente es "SI", en caso de que algún diccionario esté vacío, devolverá que
#la información suficiente es "NO".
def evaluar_informacion_suficiente(lista_clientes, lista_restaurantes, lista_rappitenderos):
    info_suficiente = False if (len(lista_clientes) == 0 or len(lista_restaurantes) == 0 or len(lista_rappitenderos) == 0) else True
    if not info_suficiente:
        print("\nNo hay suficiente información para ejecutar esta opción, pruebe cargando datos de clientes, restaurantes y rappitenderos previamente.\n")    
    return info_suficiente


# Función que recibe la opción ingresada, verifica si es un número y luego
#evalúa si el número está en el rango de opciones válidas mostradas en pantalla.
# Devuelve un string con SI en caso de ser una opcion válida, caso contrario devuelve NO.
def validar_opcion_ingresada(opcion, opcion_maxima, opcion_minima=0):
    if (opcion.isdigit() and opcion_minima<=int(opcion)<=opcion_maxima):
        opcion_correcta = True
    else:
        opcion_correcta = False
        print("\nEl dato ingresado no es válido. Ingrese un número entero entre los valores indicados.\n")
    return opcion_correcta

def imprimir_aviso_de_retorno_al_menu_anterior():
    print("\n<------------Redirigiéndolo al menú anterior.")

def solicitar_ingreso_de_opcion():
    opcion = input("\n\t\tElija una opción para continuar: ")
    return opcion

# Función que solo muestra opciones, no pide ni devuelve ningun valor.
def listar_opciones(lista_opciones):
    for i, o in enumerate(lista_opciones):
        print("\t\t",i, "-", o)    

# Función que devuelve el número entero de la opción elegida del submenú informes.
def devolver_opcion_elegida_validada_desde_lista(lista_opciones):
    opcion_valida = False
    while not opcion_valida:
        listar_opciones(lista_opciones)
        opcion_elegida = solicitar_ingreso_de_opcion()
        opcion_valida = validar_opcion_ingresada(opcion_elegida, len(lista_opciones)-1)
    return int(opcion_elegida)

def imprimir_titulo_seccion(seccion):
    print("\n--------------------{}--------------------\n".format(seccion.upper()))
    #  t = PrettyTable(['{}'.format(seccion.upper())])
    #  print (t)