# Metodología Entrega final reto MGE

Para esta entrega, utilizamos principalmente Python con el objetivo de limpiar, modelar, predecir y visualizar datos globales de los países y la producción/consumo de energía eléctrica. 


## Librerías utilizadas

- Pandas: Lectura, escritura, y manipulación de datos
- Scikit Learn: Análisis predictivo
- Matplotlib: Visualización de datos

## Estructura del proyecto

- datasets: Archivos con datos
- venv: Virtual environment

### Datasets

- output.csv: Principal dataframe utilizado en el proyecto. Incluye información de 2 años y medio del historial de producción y consumo de energías de distintos tipos por país.

## Ejecutables

Se ubican en la carpeta principal, y contienen la lógica utilizada a lo largo del proyecto.

### Ejecutables de limpieza de datos

Modifican o crean columnas en el dataframe "output.csv"

- clean_data.py: Modificación de valores NaN (principalmente valores que contienen espacios).
- percentage.py: Creación de columna nueva llamada "renewable_percentage" que permite calcular los porcentajes de energía renovable de cada país.
- date.py: Añade la columna "date" al dataframe.

### Ejecutables localizadores

Localizan elementos específicos con información relevante. Son utilizados para localizar 3 países relevantes

- greatest_increment.py: Identifica el país con el mayor incremento de GWh de energías renovables registrado.
- greatest_renewable_percentage.py: Identifica el país con el mayor porcentaje de energías renovables con respecto a las energías en general.
- greatest_renewable_value.py: Identifica el país con el mayor número de GWh producidas en un mes.

### Ejecutables de visualización

Producen visualizaciones mediante Matplotlib.pyplot

- bar_chart_percentage.py: Produce una gráfica de barras de los porcentajes de los 4 países de relevancia.
- bar_chart_renewable_increment.py: Produce una gráfica de barras de los incrementos de GWh de los 4 países de relevancia.
- linear_regression.py: Produce una gráfica de dispersión y predice y visualiza la tendencia de la cantidad de GWh producida en México.
- linear_regression_percentage.py: Produce una gráfica de dispersión y predice y visualiza la tendencia del porcentaje de energías renovables con respecto a las energías en general.
- linear_regression_per_energy: Produce gráficas de dispersión y predice y visualiza la tendencia de la cantidad de GWh producida en México.

### Ejecutable de predicción

predict.py: Predice el porcentaje 