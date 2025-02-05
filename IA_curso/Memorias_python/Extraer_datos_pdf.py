
import fitz  # PyMuPDF
import mysql.connector
import os

def extraer_datos_pdf(ruta_pdf):
    # Verificar si el archivo existe
    if not os.path.exists(ruta_pdf):
        raise FileNotFoundError(f"El archivo {ruta_pdf} no existe.")
    
    # Abrir el archivo PDF
    documento = fitz.open(ruta_pdf)
    
    # Inicializar el diccionario para guardar los datos
    datos_extraidos = {}
    
    # Recorrer todas las páginas del PDF
    for pagina_num in range(len(documento)):
        pagina = documento.load_page(pagina_num)
        texto = pagina.get_text()
        
        # Identificar y guardar datos específicos en el diccionario
        if "prueba" in texto:
            datos_extraidos["prueba"] = texto.split("prueba")[1].strip()
        if "logotipo" in texto:
            datos_extraidos["logotipo"] = texto.split("logotipo")[1].strip()
    
    return datos_extraidos

def guardar_datos_en_mysql(datos):
    # Conectar a la base de datos MySQL
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
    
    cursor = conexion.cursor()
    
    # Crear una consulta SQL para insertar los datos
    consulta = "INSERT INTO tu_tabla (columna_prueba, columna_logotipo) VALUES (%s, %s)"
    valores = (datos.get("prueba", ""), datos.get("logotipo", ""))
    
    # Ejecutar la consulta
    cursor.execute(consulta, valores)
    
    # Confirmar los cambios
    conexion.commit()
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()

# Ejemplo de uso
ruta_pdf = "Documento.pdf"
datos = extraer_datos_pdf(ruta_pdf)
print(datos)