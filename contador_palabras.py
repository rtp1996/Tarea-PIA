import string
def frecuencia_palabras(lista_palabras, ruta_fichero):

    # Crea un diccionario inicial con todas las palabras en 0
    frecuencia = {palabra.lower(): 0 for palabra in lista_palabras}
    try:
        # Abre y lee el archivo
        with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            # Elimina signos de puntuación y convertir a minúsculas
            traductor = str.maketrans('', '', string.punctuation)
            texto_limpio = contenido.translate(traductor).lower()

            # Divide el texto en palabras
            palabras_texto = texto_limpio.split()

            #Cuenta la frecuencia de cada palabra de nuestra lista
            for palabra in palabras_texto:
                if palabra in frecuencia:
                    frecuencia[palabra] += 1

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{ruta_fichero}'")
        return {}
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return {}

    return frecuencia

# Muestra los resulados ordenados alfabeticamente por palabra
def mostrar_frecuencias(diccionario_frecuencias):

    if not diccionario_frecuencias:
        print("No hay datos para mostrar")
        return
    print("-" * 60)
    print("          Frecuencia de palabras: \n ")


    # Ordena las palabras
    for palabra in sorted(diccionario_frecuencias.keys()):
        frecuencia = diccionario_frecuencias[palabra]
        print(f"{palabra}: {frecuencia}")
    print("-" * 60)

if __name__ == "__main__":
    # Lista de palabras
    palabras_buscar = ["la", "el", "texto", "Lorem", "que"]

    # Ruta del archivo (puedes cambiar esto por la ruta de tu archivo)
    ruta_archivo = "texto_ejemplo.txt"

    # Crea un archivo de ejemplo si no existe
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write("""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno 
            estándar de las industrias desde el siglo XVI, cuando un impresor (anónimo) usó una galera de tipos y los mezcló para crear un libro de 
            muestras tipográficas. Ha sobrevivido no solo cinco siglos, sino también la transición a la composición tipográfica electrónica,
             manteniéndose prácticamente inalterado. Se popularizó en la década de 1960 con la publicación de las hojas Letraset que contenían
              pasajes de Lorem Ipsum y, más recientemente, con software de autoedición como Aldus PageMaker, que incluía versiones de Lorem Ipsum.""")
        print(f"Archivo de ejemplo creado: {ruta_archivo}")
    except:
        print("Usando archivo existente...")

    # Usar nuestra función
    print(f"Buscando palabras: {palabras_buscar}")
    resultado = frecuencia_palabras(palabras_buscar, ruta_archivo)

    # Mostrar resultados
    mostrar_frecuencias(resultado)