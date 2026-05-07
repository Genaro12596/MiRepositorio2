import numpy as np
import matplotlib.pyplot as plt
# Generar valores de x
x = np.linspace(-10, 10, 10)
# Definir funciones
y1 = x**2
y2 = 2*x + 1
y3= np.power(x,3)
y4=np.sin(x)
y5=np.exp(-x)


# Crear figura
plt.figure(figsize=(10,6))

# Grafica de lınea
plt.plot(x, y1, label="y = x^2")

# Grafica de dispersion
plt.scatter(x, y2, label="y = 2x + 1")

plt.plot(x,y3,label="y=x^3")

plt.plot(x,y4,label="Y=sin(X)")

plt.plot(x,y5,label="y=e^-x")

# Etiquetas y t´ıtulo
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Graficas combinadas")
plt.legend()
plt.grid()
plt.show()