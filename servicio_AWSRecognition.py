import boto3
import os
import re
from botocore.exceptions import ClientError

def configurar_cliente_rekognition():
    try:
        cliente = boto3.client('rekognition', region_name='us-east-1')
        return cliente
    except ClientError as e:
        print(f"Error en la configuracion Rekognition: {e}")
        return None

def validar_imagen(archivo):
    """
    Verifica si la imagen es valida(formatos permitidos: .jpg,.jpeg o .png)
    """
    extensiones_validas = ['.jpg', '.png','.jpeg']
    _,extension = os.path.splitext(archivo)
    return extension.lower() in extensiones_validas

def detectar_coches(cliente,imagen_bytes):
    """
    detecta si hay coches en la imagen usando AWS Rekognition

    """
    try:
        respuesta = cliente.detect_labels(Image={'Bytes': imagen_bytes},
                                          MaxLabels=10,
                                          MinConfidence=90.0
                                          )
        etiquetas_vehiculos =['car','vehicle','automobile']
        for label in respuesta['Labels']:
            if label['Name'].lower() in etiquetas_vehiculos and label['Confidence'] >= 90:
                return True,label['Confidence']

        return False,0
    except ClientError as e:
        print(f"Error detectando coches: {e}")
        return False,0

def detectar_matriculas(cliente, imagen_bytes):
    """
    Detecta posibles matrículas en la imagen
    """
    try:
        respuesta = cliente.detect_text(
            Image={'Bytes': imagen_bytes}
        )

        matriculas_detectadas = []

        for deteccion in respuesta['TextDetections']:
            texto = deteccion['DetectedText']
            tipo = deteccion['Type']
            confianza = deteccion['Confidence']

            # Solo nos interesan líneas con confianza > 90%
            if (tipo == 'LINE' and
                    confianza >= 90.0 and
                    5 <= len(texto) <= 10):

                # Verifica que tenga al menos una letra y un número
                if (re.search(r'[A-Za-z]', texto) and
                        re.search(r'[0-9]', texto)):
                    matriculas_detectadas.append({
                        'texto': texto,
                        'confianza': confianza
                    })

        return matriculas_detectadas
    except ClientError as e:
        print(f"Error detectando matriculas: {e}")
        return []

def procesar_imagen_local(cliente, ruta_imagen):
    """
    Procesa una imagen del sistema de archivos local
    """
    try:
        with open(ruta_imagen, 'rb') as archivo:
            imagen_bytes = archivo.read()

        # Detecta si hay coches
        hay_coches, confianza = detectar_coches(cliente, imagen_bytes)

        print(f"\nImagen: {os.path.basename(ruta_imagen)}")
        print(f"¿Aparecen coches? {'SÍ' if hay_coches else 'NO'}")

        if hay_coches:
            print(f"Confianza en detección de coches: {confianza:.2f}%")

            # Detecta las matrículas
            matriculas = detectar_matriculas(cliente, imagen_bytes)

            if matriculas:
                print("Matrículas detectadas:")
                for matricula in matriculas:
                    print(f"  - {matricula['texto']} (confianza: {matricula['confianza']:.2f}%)")
            else:
                print("No se detectaron matrículas válidas")
        else:
            print("No se detectaron coches en esta imagen")

    except Exception as e:
        print(f"Error procesando imagen {ruta_imagen}: {e}")

def main():
    """
    Función principal
    """
    print("*** DETECTOR DE COCHES Y MATRÍCULAS CON AWS REKOGNITION ***")
    print("\n  Analizador imágenes para detectar coches y sus matriculas.")

    # Configura cliente de Rekognition
    print("\nEstableciendo conexión con AWS Rekognition...")
    cliente = configurar_cliente_rekognition()

    if not cliente:
        print("Error: No se pudo configurar el cliente de Rekognition")
        print("Asegúrate de tener configuradas las credenciales de AWS")
        return

    print("Conexión establecida con AWS Rekognition!!!")

    # Solicita ruta de la carpeta
    while True:
        ruta_carpeta = input("\nPor favor,Introduce la ruta de la carpeta con imágenes: ").strip()

        if os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta):
            break
        else:
            print("Error: La ruta no existe o no es una carpeta válida")
            print("Ejemplo: C:/Users/MiUsuario/Imágenes o /home/usuario/imagenes")

    # Busca imágenes en la carpeta
    print(f"\nBuscando imágenes en: {ruta_carpeta}")
    imagenes = []

    for archivo in os.listdir(ruta_carpeta):
        if validar_imagen(archivo):
            ruta_completa = os.path.join(ruta_carpeta, archivo)
            imagenes.append(ruta_completa)

    if not imagenes:
        print("No se encontraron imágenes .jpg,.jpeg o .png en la carpeta")
        return

    print(f"Se encontraron {len(imagenes)} imágenes para procesar")

    # Procesa cada imagen
    input("\nPresiona Enter para comenzar el análisis...")

    for imagen in imagenes:
        procesar_imagen_local(cliente, imagen)

    print("\n=== ANÁLISIS COMPLETADO ===")

if __name__ == "__main__":
    main()