import boto3

# Crea un cliente de S3
s3 = boto3.client('s3')

# Lista los buckets de S3
response = s3.list_buckets()

print("Buckets de S3:")
for bucket in response['Buckets']:
    print(f"Nombre del bucket: {bucket['Name']}")

