"""
Este es un ejemplo de como hacer un proceso de etl desde la computadora loca, y luego cargar este 
proceso a un bucket de S3, 
Pero hare un un ejemplo mas completo donde se hace un proceso de ETL y todo orquestado desde AWS y 
conectado desde APache Zeppelin
Recuerda configurar tus variables de entorno y ademas te comiendo que uses dbeaver-ce,para cargar
la data transformada, esto si usas AWS Redshift """

import pandas as pd
import boto3
import psycopg2
from io import StringIO

# Función para establecer la conexión a la base de datos PostgreSQL
def conectar_base_de_datos():
    db_host = 'tu-host-de-base-de-datos'
    db_port = 'tu-puerto-de-base-de-datos'  # Generalmente 5432 para PostgreSQL
    db_user = 'tu-usuario-de-base-de-datos'
    db_password = 'tu-contraseña-de-base-de-datos'
    db_database = 'tu-nombre-de-base-de-datos'
    
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database
        )
        return conn
    except psycopg2.Error as err:
        print(f"Error al conectar a la base de datos PostgreSQL: {err}")
        return None

# Función para realizar la transformación de datos
def transformar_datos(conn):
    # Consulta SQL para obtener datos de la base de datos
    sql_query = "SELECT * FROM tu_tabla_de_datos"
    
    try:
        # Ejecuta la consulta y carga los resultados en un DataFrame de Pandas
        data = pd.read_sql(sql_query, conn)
        
        # Realiza transformaciones más avanzadas en los datos
        # Cambia el DataFrame 'data' según tus necesidades
        return data
    except Exception as e:
        print(f"Error al transformar datos: {e}")
        return None


# Configuración de las credenciales de AWS y otras variables
aws_access_key_id = 'TU_ACCESS_KEY_ID'
aws_secret_access_key = 'TU_SECRET_ACCESS_KEY'
region_name = 'tu-region'  # Cambia esto a tu región de AWS
bucket_name = 'nombre-de-tu-bucket'
file_name = 'nombre-del-archivo-transformado.csv'  # Cambia esto al nombre que desees para el archivo

# Establece la conexión a la base de datos PostgreSQL
conexion_db = conectar_base_de_datos()

# Si la conexión a la base de datos fue exitosa, procede con la transformación y carga en S3
if conexion_db:
    # Realiza la transformación de datos
    datos_transformados = transformar_datos(conexion_db)

    # Cierra la conexión a la base de datos
    conexion_db.close()

    # Si la transformación de datos fue exitosa, carga los datos en S3
    if datos_transformados is not None:
        cargar_datos_en_s3(datos_transformados, aws_access_key_id, aws_secret_access_key, region_name, bucket_name, file_name)

