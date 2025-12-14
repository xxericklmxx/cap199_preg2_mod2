import pandas as pd

# Enlace directo al archivo ZIP (usando raw)
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"

# Cargar el dataset en memoria descomprimiendo al vuelo
# 'compression=zip' es la clave aquí
df = pd.read_csv(url, compression='zip')

# Verificación
print("✅ Dataset cargado correctamente en la variable 'df'")
print(f"Dimensiones del dataset: {df.shape}")
print(df.head())
