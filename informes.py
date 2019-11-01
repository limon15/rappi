from common import evaluar_informacion_suficiente, devolver_opcion_elegida_validada_desde_lista, imprimir_aviso_de_retorno_al_menu_anterior, PrettyTable


# Función que ordena asc/desc una lista de diccionario de acuerdo al valor de una clave y genera un reporte del top pedido
def mostrar_top_entidad_segun_clave_valor(lista_clientes, limit, col_to_order, id_col):
    list_sorted = reordenar_lista_de_dicc_por_valor(lista_clientes, col_to_order, True)
    generar_reporte_top(list_sorted, limit, id_col, col_to_order)

def reordenar_lista_de_dicc_por_valor(lista, clave, reverse=False):
    lista_sorted = sorted(lista, key = lambda x: x[clave], reverse=reverse)
    return lista_sorted

def generar_reporte_top(lista, limit, col1, col2):
    t = PrettyTable([col1, col2])
    i=0
    while i < len(lista) and i<limit:
        t.add_row([lista[i][col1], lista[i][col2]])
        i+=1
    print(t)

# Función encargada de mostrar algunas estadísticas de clientes, restaurantes y rappitenderos.
def informes(lista_clientes, lista_restaurantes, lista_rappitenderos):
    informacion_suficiente = evaluar_informacion_suficiente(lista_clientes, lista_restaurantes, lista_rappitenderos)
    if informacion_suficiente:
        opciones = ['Clientes con mayor Rappicreditos', 'Rappitenderos con mayor propina acumulada', 'Restaurantes que mas ventas tuvieron', 'Volver al menú principal']
        opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, 2)
        volver = len(opciones)-1
        while opcion_elegida != volver :
            if opcion_elegida == 0:
                print("\nEstos son los clientes con mayor Rappicreditos: \n")
                mostrar_top_entidad_segun_clave_valor(lista_clientes, 5, "Rappicreditos", "Nombre de usuario")
                imprimir_aviso_de_retorno_al_menu_anterior()
            elif opcion_elegida == 1:
                print("\nEstos son los rappitenderos con mayor propina acumulada: \n")
                mostrar_top_entidad_segun_clave_valor(lista_rappitenderos, 5, "Propina acumulada", "Nombre") 
                imprimir_aviso_de_retorno_al_menu_anterior()                                   
            elif opcion_elegida == 2:
                print("\nEstos son los restaurantes que más ventas tuvieron: \n")                 
                mostrar_top_entidad_segun_clave_valor(lista_restaurantes, 5, "Total de ventas", "Nombre")
                imprimir_aviso_de_retorno_al_menu_anterior()                                              
            opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, 2)
    imprimir_aviso_de_retorno_al_menu_anterior()