def operaciones_conjuntos(lista1, lista2):

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    # Convierte listas a conjuntos (elimina duplicados )
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    print(f"Conjunto 1: {conjunto1}")
    print(f"Conjunto 2: {conjunto2}")

    # Operaciones con conjuntos
    interseccion = conjunto1 & conjunto2  # Elementos comunes
    union = conjunto1 | conjunto2  # Todos los elementos
    diferencia_simetrica = conjunto1 ^ conjunto2  # En uno u otro pero no en ambos

    # Crea un diccionario de resultados.
    resultados = {
        'interseccion': sorted(list(interseccion)),  # Ordenados
        'union': sorted(list(union)),  # Ordenados
        'diferencia_simetrica': sorted(list(diferencia_simetrica))  # Ordenados
    }

    return resultados


def mostrar_resultados_conjuntos(resultados):

    print("\n" + "=" * 60)
    print("RESULTADOS DE OPERACIONES EN LOS CONJUNTOS")
    print("=" * 60)

    # - Intersección
    print("1. INTERSECCIÓN (elementos en ambos  conjuntos):")
    print(f"   Números que aparecen en los dos conjuntos")
    print(f"   {resultados['interseccion']}")


    # - Unión
    print("\n2. UNIÓN (todos los elementos sin ningún duplicado ):")
    print(f"   Números diferentes de ambos conjuntos")
    print(f"   {resultados['union']}")


    # - Diferencia simétrica
    print("\n3. DIFERENCIA SIMÉTRICA :")
    print(f"   Números que solo aparecen en un conjunto u el otro , no en ambos")
    print(f"   {resultados['diferencia_simetrica']}")


    # - Estadísticas
    print("\n" + "-" * 60)
    print(f"ESTADÍSTICAS:")
    print(f"   • Elementos comunes: {len(resultados['interseccion'])}")
    print(f"   • Elementos únicos totales: {len(resultados['union'])}")
    print(f"   • Elementos exclusivos: {len(resultados['diferencia_simetrica'])}")
    print("-" * 60)



if __name__ == "__main__":
    print("CALCULADORA DE OPERACIONES CON CONJUNTOS")
    print("diferentes ejemplos:\n")

    print(" EJEMPLO 1 ")
    lista_a = [1, 2, 3, 4, 5, 2, 3]
    lista_b = [4, 5, 6, 7, 8, 4]

    resultados1 = operaciones_conjuntos(lista_a, lista_b)
    mostrar_resultados_conjuntos(resultados1)

    # Ejemplo 2
    print("\n\n   EJEMPLO 2 ")
    lista_c = [10, 20, 30, 40, 50]
    lista_d = [30, 40, 50, 60, 70]

    resultados2 = operaciones_conjuntos(lista_c, lista_d)
    mostrar_resultados_conjuntos(resultados2)

    # Ejemplo 3
    print("\n\n    EJEMPLO 3 ")
    lista_e = [1, 3, 5, 7, 9]
    lista_f = [2, 4, 6, 8, 10]

    resultados3 = operaciones_conjuntos(lista_e, lista_f)
    mostrar_resultados_conjuntos(resultados3)
