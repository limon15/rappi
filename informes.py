from common import evaluar_informacion_suficiente, devolver_opcion_elegida_validada_desde_lista, imprimir_aviso_de_retorno_al_menu_anterior, PrettyTable, evaluar_existencia_entidad


def mostrar_top_entidad_segun_clave_valor(lista, limit, col_to_order, id_col):
    list_sorted = sorted(lista, key = lambda x: x[col_to_order], reverse=True)
    t = PrettyTable([id_col, col_to_order])
    i=0
    while i < len(list_sorted) and i<limit:
        t.add_row([list_sorted[i][id_col], list_sorted[i][col_to_order]])
        i+=1
    print(t)

# Función encargada de mostrar algunas estadísticas de clientes, restaurantes y rappitenderos.
def informes(lista_clientes, lista_restaurantes, lista_rappitenderos):
    informacion_suficiente = evaluar_informacion_suficiente(lista_clientes, lista_restaurantes, lista_rappitenderos)
    if informacion_suficiente:
        opciones = ['Clientes con mayor Rappicreditos', 'Rappitenderos con mayor propina acumulada', 'Restaurantes que mas ventas tuvieron', 'Generar csv de rappitenderos', 'Volver al menú principal']
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
            elif opcion_elegida == 3:
                generar_archivo_rappitenderos(lista_rappitenderos)
                imprimir_aviso_de_retorno_al_menu_anterior()                                                                  
            opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, 2)
    imprimir_aviso_de_retorno_al_menu_anterior()

def generar_archivo_rappitenderos(lista_rappitenderos):
    f = open("rappitenderos.csv", "w")
    for i in range(len(lista_rappitenderos)):
        f.write(f"{lista_rappitenderos[i]['Nombre']},{lista_rappitenderos[i]['Distancia recorrida']}\r\n")
    f.close()    
    print("\nSe generó satisfactoriamente el archivo rappitenderos.csv\n")  