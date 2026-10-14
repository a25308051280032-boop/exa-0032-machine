print("Iris Chavez Machine Learning pandas, NC 0032")
import sys
import os
import pandas as pd

# Permitir importar dicc-0032.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0032')))
import dicc_0032

print("Iris Chavez Machine Learning pandas, NC 0032")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Iris Chavez Machine Learning pandas, NC 0032"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0032.datos_animales)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Animal)
registrar("3. Estadísticas Generales de la Columna 'Animal'", df['Animal'].describe())

# 4. Ordenar Ascendente por Precio
df_asc_precio = df.sort_values(by="Animal", ascending=True)
registrar("4. Ordenar Ascendente por Animal", df_asc_precio)

# 5. Ordenar Descendente por Stock
df_desc_stock = df.sort_values(by="Stock", ascending=False)
registrar("5. Ordenar Descendente por Stock", df_desc_stock)

# 7. Guardar el archivo resultados-ml-0032.md dentro de resultados-0032
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0777'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0032.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("+-+-+-+-+-+-+--+-+-+")

print("Iris Chavez Machine Learning pandas, NC 0032")
print("+-+-+-+-+-+--+-+-+--+-")

datos_animales = {
    "Animal": ["León", "Tigre", "Elefante", "Jirafa", "Cebra", "Rinoceronte"],
    "Peso_kg": [190, 220, 5000, 800, 350, 1500],
    "Velocidad_kmh": [80, 65, 40, 55, 65, 50]
} 

print("+-+-+-+-+-+--+-+-+--+-")
print("Iris Chavez Machine Learning pandas, NC 0032")
