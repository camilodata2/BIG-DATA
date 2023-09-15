from raw_data import *
from io import StringIO
# Función para cargar datos en un bucket de S3
def cargar_datos_en_s3(data, aws_access_key_id, aws_secret_access_key, region_name, bucket_name, file_name):
    # Convierte el DataFrame en una cadena CSV
    csv_buffer = StringIO()
    data.to_csv(csv_buffer, index=False)
    
    try:
        # Crea un cliente de S3
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        
        # Carga los datos transformados en un bucket de S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
        
        print(f'Datos transformados cargados en s3://{bucket_name}/{file_name}')
    except Exception as e:
        print(f"Error al cargar datos en S3: {e}")
