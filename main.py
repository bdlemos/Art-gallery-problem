# TRABALHO PRATICO 1 - TRIANGULACAO DE POLIGONOS
import numpy as np
import sys
from polygon import Polygon
from Coloring import Coloring

def read_polygon(file):
    vertices = []
    with open(file, 'r') as f:
        content = f.read().replace('\n',' ').split(' ')
        for v in content[1:]:
            v = v.split('/')
            vertices += [float(v[0])/int(v[1])] if len(v) > 1 else []

    return np.array([vertices[i:i+2] for i in range(0, len(vertices), 2)])



if __name__ == "__main__":
    for name in sys.argv[1:]:
        polygon = read_polygon(name)

        polygon = Polygon(polygon)
        coloring = Coloring(polygon)
        polygon.plot_polygon(coloring.get_colored_vertex_list())
    