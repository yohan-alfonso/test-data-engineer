import csv
import psycopg2
from datetime import datetime


# Parámetros de conexión a la base de datos PostgreSQL
db_params = {
    'dbname': 'awto',
    'user': 'yohan',
    'password': 'yohan_pass',
    'host': 'localhost',
    'port': '5431'
}

# Ruta del archivo CSV
csv_file_path = 'trips.csv'

# Conexión a la base de datos
try:
    conn = psycopg2.connect(**db_params)
    print("Conexión exitosa a la base de datos")
except psycopg2.Error as e:
    print("Error: No se pudo conectar a la base de datos")
    print(e)
    exit()

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Leer el archivo CSV e insertar datos en la tabla "Users"
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Saltar la primera fila (encabezados del CSV)
    for row in csvreader:
        
        # inserta users
        query = "INSERT INTO Users (user_id, name_user, rut_user) VALUES (%s, %s, %s)"
        cursor.execute(query, (int(row[0]), row[1], row[3]))

        vehicle_id = int(row[0])  # Assuming the first column of the CSV contains vehicle_id
        insert_query = "INSERT INTO Vehicles (vehicle_id) VALUES (%s)"
        cursor.execute(insert_query, (vehicle_id,))

        #Insserta status
        status_id = int(row[0])  # Assuming the first column of the CSV contains vehicle_id
        insert_query = "INSERT INTO Status (status_id) VALUES (%s)"
        cursor.execute(insert_query, (status_id,))
        
        #inserta membership
        membership_id = int(row[0])  # Assuming the first column of the CSV contains vehicle_id
        insert_query = "INSERT INTO Memberships (membership_id) VALUES (%s)"
        cursor.execute(insert_query, (status_id,))
        
        #inserta trips
        iso_format = "%Y-%m-%d %H:%M:%S"
        # Create POINT values as strings
        start_location = f"({float(row[14])}, {float(row[15])})"
        end_location = f"({float(row[16])}, {float(row[17])})"
        
        trip_id = int(row[0])
        user_id = int(row[1])
        vehicle_id = str(row[4])
        booking_time = datetime.strptime(row[5], iso_format)
        start_time = datetime.strptime(row[6], iso_format)
        end_time = datetime.strptime(row[7], iso_format)
        travel_dist = float(row[9])
        membership_id = int(row[10])
        status_id = int(row[8])
        price_amount = float(row[11])
        price_tax = float(row[12])
        price_total = float(row[13])
        start_location  
        end_location  
       
        insert_query = "INSERT INTO Trips (trip_id, user_id, vehicle_id, booking_time, start_time, end_time, travel_dist,\
            membership_id, status_id, price_amount, price_tax, price_total, start_location, end_location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            insert_query,
            (trip_id, user_id, vehicle_id, booking_time, start_time, end_time, travel_dist, membership_id,
             status_id, price_amount, price_tax, price_total, start_location, end_location)
        )

        
# Hacer commit para guardar los cambios
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente en la tabla Users.")
