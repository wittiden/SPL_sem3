import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure('Matplotlib')
ax = fig.add_subplot(projection='3d')
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
# Z = X**0.25 + Y**0.25
Z = X**2 - Y**2
# Z = 2*X + 3*Y
# Z = 2 + 2*X + 2*Y - X**2 - Y**2
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()

