def procesar_lista(lista_enteros):
    # 1. Elimina los números negativos
    lista_sin_negativos = [num for num in lista_enteros if num >= 0]

    # 2. Elimina números duplicados
    lista_sin_duplicados = []
    for elemento in lista_sin_negativos:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    # 3. Ordena la lista de menor a mayor
    lista_sin_duplicados.sort()
    return lista_sin_duplicados

print(procesar_lista([4, -1, 2, 4, 3, -5, 2]))