import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"
df = pd.read_csv(url, compression='zip')

# Visualización
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# 1. Edad
axes[0, 0].hist(df['age'], bins=5, color='skyblue', edgecolor='black', alpha=0.8)
axes[0, 0].set_title('Distribucion de la edad')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].grid(True, alpha=0.3)

# 2. Genero
conteo_genero = df['gender'].value_counts()
axes[0, 1].pie(conteo_genero, labels=conteo_genero.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Distribucion del genero')

# 3. Pais
conteo_paises = df['country'].value_counts()
axes[1, 0].bar(conteo_paises.index, conteo_paises.values, color='lightcoral')
axes[1, 0].set_title('Pacientes por pais')
axes[1, 0].set_ylabel('Numero de pacientes')
axes[1, 0].tick_params(axis='x', rotation=90)

# 4. Etapa
conteo_etapa = df['cancer_stage'].value_counts()
axes[1, 1].bar(conteo_etapa.index, conteo_etapa.values, color='lightgreen')
axes[1, 1].set_title('Distrbucion de la etapa del cancer')
axes[1, 1].set_ylabel('Numero de Observaciones')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('grafico_cancer_completo.png') # Guardamos la imagen tambien
plt.show()
