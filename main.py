# TRABALHO PRATICO 1 - TRIANGULACAO DE POLIGONOS
import numpy as np
import sys
from polygon import Polygon
from Coloring import Coloring
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.animation import FuncAnimation

def read_polygon(file):
    vertices = []
    with open(file, 'r') as f:
        content = f.read().replace('\n',' ').split(' ')
        for v in content[1:]:
            v = v.split('/')
            vertices += [float(v[0])/int(v[1])] if len(v) > 1 else []

    return np.array([vertices[i:i+2] for i in range(0, len(vertices), 2)])

def plot_plt(polygon, triangles, coloring):
    fig, ax = plt.subplots()
    ax.set_xlim(min(polygon[:, 0]) - 5, max(polygon[:, 0]) + 5)
    ax.set_ylim(min(polygon[:, 1]) - 5, max(polygon[:, 1]) + 5)
    ax.set_aspect('equal')
    dfs_order = sorted(coloring.get_dual_graph_vertex(), key=lambda point: point[1])

    for tri in triangles:
        triangle = patches.Polygon(tri, closed=True, edgecolor='gray', facecolor='lightgreen')
        ax.add_patch(triangle)

    def init():
        for tri in triangles:
            triangle = patches.Polygon(tri, closed=True, edgecolor='gray', facecolor='lightgreen')
            ax.add_patch(triangle)
        return ax.patches

    def animate(i):
        ax.clear()
        ax.set_xlim(min(polygon[:, 0]) - 5, max(polygon[:, 0]) + 5)
        ax.set_ylim(min(polygon[:, 1]) - 5, max(polygon[:, 1]) + 5)
        ax.set_aspect('equal')

        for tri in triangles:
            triangle = patches.Polygon(tri, closed=True, edgecolor='gray', facecolor='lightgreen')
            ax.add_patch(triangle)

        for vertex in dfs_order[:i+1]:
            for nb in coloring.dual_graph_adj_list[vertex[0]]:
                triangle = triangles[vertex[0]]
                triangle_nb = triangles[nb]
                baricenter = np.mean(triangle[:3], axis=0)
                baricenter_nb = np.mean(triangle_nb[:3], axis=0)

                ax.plot([baricenter[0], baricenter_nb[0]], [baricenter[1], baricenter_nb[1]], color='black')
                ax.plot(baricenter[0], baricenter[1], 'o', markersize=2, color='black')
                ax.plot(baricenter_nb[0], baricenter_nb[1], 'o', markersize=2, color='black')

                colors = ['red', 'blue', 'green']
                for point in triangle_nb[:3]:
                    coloring_index = coloring.point_index(point)
                    ax.plot(point[0], point[1], 'o', markersize=2, color=colors[coloring.colored_vertex_list[coloring_index][1] - 1])

        return ax.patches

    ani = FuncAnimation(fig, animate, frames=len(dfs_order), init_func=init, blit=True, repeat=True, interval=1000)

    plt.show()
    ani.save('animation.gif', writer='pillow', fps=5)



if __name__ == "__main__":
    for name in sys.argv[1:]:
        polygon = read_polygon(name)

        polygon = Polygon(polygon)
        coloring = Coloring(polygon)
        polygon.plot_polygon(coloring.get_colored_vertex_list())
        plot_plt(polygon.get_vertices(), polygon.get_triangles(), coloring)
    