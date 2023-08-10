# Test Data Engineer

El desafío consiste en crear una base de datos en Postgres usando Docker, cargar los datos del archivo `trips.csv` en las tablas que considere correspondientes y realizar algunas operaciones con los datos.

El archivo `trips.csv` contiene información simulada de viajes realizados en Awto. Cada fila está representada por un viaje. Las columnas corresponden a:

- `trip_id`: Identificador único del viaje. Es un número o cadena que permite diferenciar cada viaje de manera única.
- `user_id`: Identificador del usuario que realizó el viaje. Es un valor único asociado a cada usuario.
- `name_user`: Nombre del usuario que realizó el viaje.
- `rut_user`: RUT (Rol Único Tributario) del usuario que realizó el viaje.
- `vehicle_id`: Identificador del vehículo utilizado en el viaje.
- `booking_time`: Fecha y hora en la que se realizó la reserva del viaje.
- `start_time`: Fecha y hora de inicio del viaje.
- `end_time`: Fecha y hora de finalización del viaje.
- `status_id`: Estado del viaje. Puede indicar si el viaje está en curso, completado, cancelado, etc.
- `travel_dist`: Distancia en metros recorrida en el viaje, generalmente expresada en kilómetros.
- `membership_id`: Identificador de membresía asociado al usuario que realizó el viaje.
- `price_amount`: Monto del precio del viaje (sin impuestos).
- `price_tax`: Monto de impuestos aplicados al precio del viaje.
- `price_total`: Monto total del precio del viaje (incluyendo impuestos).
- `start_lat`: Latitud de la ubicación de inicio del viaje.
- `start_lon`: Longitud de la ubicación de inicio del viaje.
- `end_lat`: Latitud de la ubicación de finalización del viaje.
- `end_lon`: Longitud de la ubicación de finalización del viaje.

A continuación, usted debe:

1. Diseñar un modelo de datos. Genere una propuesta sobre cómo guardar los datos. Justifique esa propuesta y explique por qué es la mejor opción.

2. Crea una base de datos en Postgres usando Docker.

3. Crea las tablas del modelo de datos que diseñaste en el paso 1. Puede usar scripts SQL o código en Python.

4. Genera archivos en Python para cargar los datos del archivo `trips.csv` en las tablas que creaste en el paso anterior.

5. Cree una nueva tabla en Postgres llamada `resumen_diario`.

   1. Genera con Python un proceso de ETL que cargue en la tabla un resumen por día de:
      - la cantidad de viajes
      - los suma de ingresos
      - el promedio de ingresos
      - la suma de metros recorridos.
        Explique y justifique las decisiones que tomó para generar el resumen. Considere que diariamente no habrá más de 100.000 viajes.
   2. Señale (sin necesidad de implementar) qué procesos podría desarrollar para asegurar la consistencia de los datos en la tabla `resumen_diario`.
   3. Señale (sin necesidad de implementar) cómo podría automatizar este proceso de ETL de manera diaria.

6. La empresa quiere implementar un sistema de descuentos mediante cupones. ¿Cómo modificarías el modelo de datos para agregarlo? Describa su propuesta, justifique y explique por qué es la mejor opción. No es necesario que lo implemente.

Suba todo el código a un repositorio en GitHub. Genere un archivo `README.md` que responda y explique lo requerido en los ejercicios anteriores. Declare si ocupó algún asistente de código (ChatGPT, GitHub Copilot, TabNine) y de qué manera lo ayudó a resolver el problema en caso de haberlo usado.

Envíe el link del repositorio a la persona que le envió este desafío.

Se evaluará la calidad del código, la claridad de las explicaciones y las soluciones propuestas.
