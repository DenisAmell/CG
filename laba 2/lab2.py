import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1.5, 0.86, 0],
    [1, 1.73, 0],
    [0, 1.73, 0],
    [-0.5, 0.86, 0],
    [0.5, 0.58, 1]
])

faces = [
    [0, 1, 6],
    [1, 2, 6],
    [2, 3, 6],
    [3, 4, 6],
    [4, 5, 6],
    [5, 0, 6],
    [0, 1, 2, 3, 4, 5]
]

# Create the 3D plot
pyramid = Poly3DCollection([vertices[face] for face in faces], alpha=1, facecolor='orange', linewidths=1, edgecolors='r')
ax.add_collection3d(pyramid)
ax.auto_scale_xyz([-1, 2], [-1, 2], [-1, 2])

plt.show()
