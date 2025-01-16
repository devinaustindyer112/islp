import numpy as np
from matplotlib.pyplot import subplots
import matplotlib.pyplot as plt

A = np.arange(16).reshape((4,4))

keep_rows = np.zeros(A.shape[0], bool)
keep_rows[[1,3]] = True

print(np.array([0,1,0,1]))
print(np.array([0,1,0,1]) == keep_rows)

fig, ax = subplots(figsize=(4,4))
ax.plot([1,1,0], [0,1,1])
plt.show()

# https://stackoverflow.com/questions/49944871/deactivate-a-pipenv-environment/51075851#51075851

