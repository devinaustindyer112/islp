import numpy as np
from matplotlib.pyplot import subplots

rng = np.random.default_rng(3)
x = rng.standard_normal(100) 
y = rng.standard_normal(100) 

fig, ax = subplots(figsize=(8, 8))
x = np.linspace(-np.pi, np.pi, 50)
y=x
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2)) 
ax.contour(x, y, f, levels=100)

A1 = np.arange(16).reshape(4,4)
print(A1)

A2 = np.arange(16).reshape(4,4)
print(A2)

# https://stackoverflow.com/questions/49944871/deactivate-a-pipenv-environment/51075851#51075851

