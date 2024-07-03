import numpy as np
from tqdm import tqdm
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def is_point_inside_triangle(p, p0, p1, p2):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    # Checa
    b1 = sign(p, p0, p1) >= 0.0
    b2 = sign(p, p1, p2) >= 0.0
    b3 = sign(p, p2, p0) >= 0.0

    # Check if the point is on the same side or exactly on the edge in the opposite direction
    b1_opposite = sign(p, p0, p1) <= 0.0
    b2_opposite = sign(p, p1, p2) <= 0.0
    b3_opposite = sign(p, p2, p0) <= 0.0

    # The point is inside or on the triangle if all checks are true in either direction
    return ((b1 and b2 and b3) or (b1_opposite and b2_opposite and b3_opposite))

    
def is_turn_left(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) > 0

class Polygon:
    def __init__(self, vertices):
        """
        Initialize the Polygon object.
        
        Parameters:
        vertices (numpy.ndarray): An array of shape (n, 2) where n is the number of vertices of the polygon.
        """
        self.vertices = vertices
        self.triangles = []
        self.frames = []
        self.fig = make_subplots(rows=1, cols=2, subplot_titles=("Polygon", "Current Triangle"))
        self.ear_clipping(vertices)

    
    def ear_clipping(self,polygon):
        """
        Triangulate a given polygon.

        Parameters:
        polygon (numpy.ndarray): An array of shape (n, 2) where n is the number of vertices of the polygon.

        Returns:
        tuple: A tuple containing:
            - triangles (list): A list of triangles, each triangle is a list of 4 points (the last point is the same as the first).
            - frames (list): A list of "frames", each frame is a tuple of two numpy arrays of shape (n,) representing the x and y coordinates of the polygon, less the points that have been removed.
        """
        
        def is_ear(polygon, i):
            if not is_turn_left(polygon[i-1], polygon[i], polygon[(i+1)%len(polygon)]):
                return False
            p0 = polygon[i-1]
            p1 = polygon[i]
            p2 = polygon[(i+1)%len(polygon)]
            for j in range(len(polygon)):
                if j == i or j == i-1 or j == (i+1)%len(polygon):
                    continue
                if is_point_inside_triangle(polygon[j], p0, p1, p2):
                    # print(f"Point {polygon[j]} is inside triangle {p0}, {p1}, {p2}")
                    return False
            return True
        
        def remove_ear(polygon, i):
            return np.delete(polygon, i, axis=0)
        
        self.vertices = polygon
        triangles = []
        frames = []
        initial_length = len(polygon)

        for _ in tqdm(range(initial_length - 3), desc="Processing Polygon"):
            for i in range(len(polygon)):
                if is_ear(polygon, i):
                    triangles.append([polygon[i-1], polygon[i], polygon[(i+1)%len(polygon)], polygon[i-1]])
                    aux_polygon = np.append(polygon, [polygon[0]], axis=0)
                    frames.append((aux_polygon[:,0], aux_polygon[:,1]))
                    polygon = remove_ear(polygon, i)
                    break
            else:
                print(polygon)
        
        triangles.append([polygon[0], polygon[1], polygon[2], polygon[0]])
        aux_polygon = np.append(polygon, [polygon[0]], axis=0)
        frames.append((aux_polygon[:,0], aux_polygon[:,1]))

        self.triangles = triangles
        self.frames = frames

    def plot_polygon(self):
        """
        Plot the polygon and the triangles.
        """
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Polygon", "Current Triangle"))


        # Set up the frames for animation
        for i, frame in enumerate(self.frames):
            fig.add_trace(go.Scatter(x=frame[0], y=frame[1], mode="lines+markers", name=f"Iteraçao - {i+1}", 
                                    marker=dict(color="blue"), line=dict(color="black", width=0.3)), row=1, col=1)
            x = [x for x, _ in self.triangles[i]]
            y = [y for _, y in self.triangles[i]]
            fig.add_trace(go.Scatter(x=x,
                        y=y,mode="lines+markers", name=f"Triangulo - {i+1}",
                        marker=dict(color="blue"), line=dict(color="black", width=0.3), fill="toself", fillcolor='lightgray'), row=1, col=2)

        # Slider
        steps = []
        for i in range(0,len(fig.data),2):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(fig.data)},
                    {"title": f"Frame {(i)/2}"}],
            )

            # Update the visible traces
            # Only the last in plot 1 and all traces in plot 2
            step["args"][0]["visible"][i] = True
            for j in range(1,i+2,2):
                step["args"][0]["visible"][j] = True
            steps.append(step)


        # Add layout with buttons and sliders
        fig.update_layout(
            title_text="Triangulaçao de Poligonos",
            xaxis1=dict(range=[min(self.vertices[:, 0]) - 5, max(self.vertices[:, 0]) + 5]),
            yaxis1=dict(range=[min(self.vertices[:, 1]) - 5, max(self.vertices[:, 1]) + 5]),
            xaxis2=dict(range=[min(self.vertices[:, 0]) - 5, max(self.vertices[:, 0]) + 5]),
            yaxis2=dict(range=[min(self.vertices[:, 1]) - 5, max(self.vertices[:, 1]) + 5]),
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 300, "redraw": False}, "fromcurrent": True, "transition": {"duration": 5}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    },
                    {
                        "args": [None, {"frame": {"duration": 300, "redraw": False}, "fromcurrent": True, "direction": "reverse", "transition": {"duration": 5}}],
                        "label": "Retrocede",
                        "method": "animate"
                    },
                    {
                        "args": [{"visible": [True, True]}],  # Both traces will be visible
                        "label": "Show All",
                        "method": "update"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": True,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }],
            sliders=[{
                "active": 0,
                "yanchor": "top",
                "xanchor": "left",
                "currentvalue": {
                    "font": {"size": 20},
                    "prefix": "Frame:",
                    "visible": True,
                    "xanchor": "right"
                },
                "transition": {"duration": 300, "easing": "cubic-in-out"},
                "pad": {"b": 10, "t": 50},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": steps
            }]
        )

        # Show the figure
        fig.show()
