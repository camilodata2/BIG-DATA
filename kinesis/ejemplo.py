import boto3
import json

# Configura la conexión a Kinesis
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Genera un registro de actividad
activity_log = {
    'user_id': '123',
    'action': 'login',
    'timestamp': '2023-09-11T10:30:00'
}

# Envía el registro al stream de Kinesis
response = kinesis_client.put_record(
    StreamName='my-activity-logs',
    Data=json.dumps(activity_log),
    PartitionKey='123'
)
