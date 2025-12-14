import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"
df = pd.read_csv(url, compression='zip')

# Crear Gráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Análisis de Distribución (Boxplots)', fontsize=16, fontweight='bold')

variables = ['age', 'bmi', 'cholesterol_level']
colores = ['skyblue', 'lightgreen', 'salmon']
titulos = ['Edad', 'BMI', 'Colesterol']

for i, var in enumerate(variables):
    sns.boxplot(y=df[var], ax=axes[i], color=colores[i])
    axes[i].set_title(titulos[i])
    axes[i].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Guardar la imagen para que se vea en el repo
plt.savefig('boxplots_resultado.png')
print("Imagen generada correctamente.")
