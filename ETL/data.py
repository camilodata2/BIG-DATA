import pandas as pd
from faker import Faker

# Crear una instancia de Faker
fake = Faker()

# Definir un diccionario con las columnas de datos
data_columns = {
    "Nombre": [],
    "Dirección": [],
    "Email": [],
    "Teléfono": []
}

# Generar datos ficticios y llenar el diccionario
num_filas = 10000
for _ in range(num_filas):
    data_columns["Nombre"].append(fake.name())
    data_columns["Dirección"].append(fake.address())
    data_columns["Email"].append(fake.email())
    data_columns["Teléfono"].append(fake.phone_number())

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data_columns)

# Guardar el DataFrame en un archivo CSV
nombre_archivo = "datos_ficticios.csv"
df.to_csv(nombre_archivo, index=False)

print(f"Archivo CSV creado con {num_filas} datos ficticios en '{nombre_archivo}'.")
