import json

def lambda_handler(event, context):
    for record in event['Records']:
        data = json.loads(record['kinesis']['data'])
        user_id = data['user_id']
        action = data['action']
        timestamp = data['timestamp']

        # Realiza el procesamiento deseado, como almacenar en una base de datos o generar estadísticas
        print(f"Usuario {user_id} realizó la acción {action} a las {timestamp}")
