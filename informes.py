from common import *

# Función que solo muestra los restaurantes de mayor total de ventas ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_mejores_restaurantes_en_ventas(lista_restaurantes):
    dic_aux = sorted(lista_restaurantes, key = lambda x: x['Total de ventas'], reverse=True)
    for i in range(0, len(lista_restaurantes)):
        print(f"El restaurante {dic_aux[i]['Nombre']} tiene $ {dic_aux[i]['Total de ventas']} como total de ventas.")

# Función que solo muestra los clientes de mayor rappicréditos ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_clientes_mayor_rappicreditos(lista_clientes):
    dic_aux = sorted(lista_clientes, key = lambda x: x['Rappicreditos'], reverse=True)
    i = 0
    while i < len(dic_aux) and i<10:
        print(f"-> El cliente {dic_aux[i]['Nombre de usuario']} tiene {dic_aux[i]['Rappicreditos']} rappicréditos.")
        i+=1

# Función que solo muestra los rappitenderos de mayor propina ordenados
#descententemente , no pide ni devuelve ningun valor.
def mostrar_rappitenderos_mayor_propina(lista_rappitenderos):
    dic_aux = sorted(lista_rappitenderos, key = lambda x: x['Propina acumulada'], reverse=True)
    i=0
    while i < len(dic_aux) and i<10:
        print(f"El rappitendero {dic_aux[i]['Nombre']} tiene $ {dic_aux[i]['Propina acumulada']} de propina acumulada.")
        i+=1  

# Función encargada de mostrar algunas estadísticas de clientes, restaurantes y rappitenderos.
def informes(lista_clientes, lista_restaurantes, lista_rappitenderos):
    informacion_suficiente = evaluar_informacion_suficiente(lista_clientes, lista_restaurantes, lista_rappitenderos)
    if informacion_suficiente:
        opciones = ['Clientes con mayor Rappicreditos', 'Rappitenderos con mayor propina acumulada', 'Restaurantes que mas ventas tuvieron', 'Volver al menú principal']
        opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones)
        volver = len(opciones)-1
        while opcion_elegida != volver :
            if opcion_elegida == 0:
                mostrar_clientes_mayor_rappicreditos(lista_clientes)
            elif opcion_elegida == 1:
                mostrar_rappitenderos_mayor_propina(lista_rappitenderos)
            elif opcion_elegida == 2:
                mostrar_mejores_restaurantes_en_ventas(lista_restaurantes)                                
            opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones)
        imprimir_aviso_de_retorno_al_menu_anterior()
    else:   
        imprimir_aviso_de_retorno_al_menu_anterior()