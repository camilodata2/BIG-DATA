import boto3

def ejecutar_consulta_athena(region, base_de_datos, tabla, query):
    athena = boto3.client('athena', region_name=region)

    try:
        response = athena.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': base_de_datos},
            ResultConfiguration={'OutputLocation': 's3://tu-bucket-de-resultados/'}
        )

        query_execution_id = response['QueryExecutionId']

        while True:
            query_status = athena.get_query_execution(QueryExecutionId=query_execution_id)
            status = query_status['QueryExecution']['Status']['State']
            
            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                break

        if status == 'SUCCEEDED':
            results = athena.get_query_results(QueryExecutionId=query_execution_id)
            return [row['Data'] for row in results['ResultSet']['Rows']]
        else:
            return f"La consulta ha fallado con estado: {status}"

    except Exception as e:
        return f"Error: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    region = 'tu_region'
    base_de_datos = 'tu_base_de_datos'
    tabla = 'tu_tabla'
    query = "SELECT * FROM tu_base_de_datos.tu_tabla LIMIT 10"

    resultados = ejecutar_consulta_athena(region, base_de_datos, tabla, query)

    if isinstance(resultados, list):
        for row in resultados:
            print(row)
    else:
        print(resultados)
