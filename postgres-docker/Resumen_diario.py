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

# Crear la tabla resumen_diario si no existe
create_table_query = """
    CREATE TABLE IF NOT EXISTS resumen_diario (
        año text ,
        mes text,
        day text,
        cantidad_viajes INTEGER,
        suma_ingresos FLOAT,
        promedio_ingresos FLOAT,
        suma_metros_recorridos FLOAT
    )
"""
cursor.execute(create_table_query)
conn.commit()

#ETL
#Extracción

#-- Extraer la fecha mas reciente de la fuente de información en una variable
#-- realizar una función loop para que extraiga los datos mas recientes por dia y los ingeste en la base de datos
#-- Programar un crontab diario para que los datos sean ingestados en batch
#-- Si se necetan los datos en near-real time la programación puede ser mas seguida y se necesitara un time stamp en el origen


# Generar el resumen diario y cargarlo en la tabla resumen_diario
insert_query = """
        INSERT INTO resumen_diario (año. mes. dia, cantidad_viajes, suma_ingresos, promedio_ingresos, suma_metros_recorridos)
        select
            extract(year from start_time) as año,
            extract(month from start_time) as mes,
            extract(day from start_time) as dia,
            COUNT(*) AS cantidad_viajes,
            SUM(price_total) AS suma_ingresos,
            AVG(price_total) AS promedio_ingresos,
            SUM(travel_dist) AS suma_metros_recorridos
            FROM trips
            group by dia,año, mes
            order by año, mes, dia asc
    """
cursor.execute(insert_query)
conn.commit()
    

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

print("Resumen diario generado y cargado en la tabla resumen_diario.")
