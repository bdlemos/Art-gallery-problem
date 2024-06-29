# TRABALHO PRATICO 1 - TRIANGULACAO DE POLIGONOS
import numpy as np
import sys
from polygon import Polygon

def read_polygon(file):
    vertices = []
    with open(file, 'r') as f:
        content = f.read().split(' ')
        for v in content[1:]:
            v = v.split('/')
            vertices += [float(v[0])/int(v[1])] if len(v) > 1 else []

    return np.array([vertices[i:i+2] for i in range(0, len(vertices), 2)])


# def plot_triangles(triangles, ax):
#     for triangle in triangles:
#         ax.plot([triangle[0][0], triangle[1][0], triangle[2][0], triangle[0][0]],
#             [triangle[0][1], triangle[1][1], triangle[2][1], triangle[0][1]],
#             color='b', linestyle='-', linewidth=0.4)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        polygon = read_polygon(name)
        polygon = np.append(polygon, [polygon[0]], axis=0)

        polygon = Polygon(polygon)
        polygon.plot_polygon()
    