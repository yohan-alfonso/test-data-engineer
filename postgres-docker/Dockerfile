# Use the official PostgreSQL image as the base image
FROM postgres

# Set environment variables

ENV POSTGRES_PASSWORD yohan_pass
ENV POSTGRES_USER  yohan
ENV POSTGRES_DB awto
ENV POSTGRES_INITDB_ARGS=--auth-host=scram-sha-256


# Opcional: Copia un archivo SQL de inicialización (puedes cargar estructura y datos desde aquí)
COPY init.sql /docker-entrypoint-initdb.d/

# Opcional: Establece el conjunto de caracteres y la configuración regional
 ENV LANG C.UTF-8

# Opcional: Copia un archivo CSV con datos para cargarlo en la base de datos (puedes cargar datos desde aquí)
COPY trips.csv .

# Puerto en el que escucha PostgreSQL dentro del contenedor (por defecto es 5432)
EXPOSE 5432
