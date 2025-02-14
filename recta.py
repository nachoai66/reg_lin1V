import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(-100,100)
y=2*x
y_1=-3*x
#Trazamos la gráfica x,y

plt.plot(x,y,'r')
plt.plot(x,y_1,'b',)
plt.title('Gráfica de la función y=2x e y=-3x')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()