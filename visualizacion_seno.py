import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x_plot = np.linspace(-0.5, 2*np.pi + 0.5, 400)
puntos_tangencia = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
colores = ['red', 'green', 'blue', 'magenta', 'cyan']
etiquetas_puntos = ['0', 'π/4', 'π/2', 'π', '3π/2']

plt.figure(figsize=(12, 6))
plt.plot(x_plot, f(x_plot), 'k-', linewidth=2.5, alpha=0.7, label='f(x) = sin(x)')

for i, a in enumerate(puntos_tangencia):
    x_tan = np.linspace(a - 1, a + 1, 100)
    y_tan = f(a) + df(a) * (x_tan - a)
    plt.plot(x_tan, y_tan, color=colores[i], linewidth=2, label=f'Tangente en x={etiquetas_puntos[i]}')
    plt.plot(a, f(a), marker='o', markersize=8, color=colores[i])

plt.title('Rectas tangentes a f(x) = sin(x)', fontsize=14, fontweight='bold')
plt.xlabel('X', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right')
plt.xlim(-0.5, 6.5)
plt.ylim(-1.1, 1.6)
plt.show()
