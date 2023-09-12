import boto3
import time

# Especifica el nombre de la región donde se encuentra tu stream de Kinesis
region_name = 'us-east-1'

# Especifica el nombre de tu stream de Kinesis
stream_name = 'mi-stream'  # Reemplaza con el nombre de tu stream de Kinesis

try:
    # Crea una conexión al servicio Kinesis
    kinesis_client = boto3.client('kinesis', region_name=region_name)

    # Crea un consumidor de Kinesis usando la Kinesis Client Library (KCL)
    from amazon_kclpy import kcl
    import sys

    class WordCounterRecordProcessor(kcl.RecordProcessorBase):
        def __init__(self):
            super(WordCounterRecordProcessor, self).__init__()

        def initialize(self, initialize_input):
            pass

        def process_records(self, process_records_input):
            for record in process_records_input.records:
                data = record.data.decode('utf-8')
                words = data.split()
                word_to_count = 'example'  # Reemplaza con la palabra que deseas contar
                count = words.count(word_to_count)
                print(f"La palabra '{word_to_count}' aparece {count} veces en el registro.")
            return kcl.Checkpointer.SUCCESS

        def shutdown(self, shutdown_input):
            pass

    # Configura y ejecuta el consumidor
    if __name__ == '__main__':
        kcl_process = kcl.KCLProcess(WordCounterRecordProcessor())
        kcl_process.run()
except Exception as e:
    print(f"Error de conexión a Kinesis: {str(e)}")
    # Puedes agregar aquí un código de manejo de excepciones específico según tus necesidades
