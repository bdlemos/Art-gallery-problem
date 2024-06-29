import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_polygon(polygon, triangles, frames):
    """
    Plot the polygon and the triangles.
    
    Parameters:
    polygon (numpy.ndarray): An array of shape (n, 2) where n is the number of vertices of the polygon.
    triangles (list): A list of triangles, each triangle is a list of 4 points (the last point is the same as the first).
    frames (list): A list of "frames", each frame is a tuple of two numpy arrays of shape (n,) representing the x and y coordinates of the polygon, less the points that have been removed.
    """
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Polygon", "Current Triangle"))


    # Set up the frames for animation
    for i, frame in enumerate(frames):
        fig.add_trace(go.Scatter(x=frame[0], y=frame[1], mode="lines+markers", name=f"Iteraçao - {i+1}", 
                                 marker=dict(color="blue"), line=dict(color="black", width=0.3)), row=1, col=1)
        x = [x for x, _ in triangles[i]]
        y = [y for _, y in triangles[i]]
        fig.add_trace(go.Scatter(x=x,
                      y=y,mode="lines+markers", name=f"Triangulo - {i+1}",
                      marker=dict(color="blue"), line=dict(color="black", width=0.3)), row=1, col=2)

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
        xaxis1=dict(range=[min(polygon[:, 0]) - 5, max(polygon[:, 0]) + 5]),
        yaxis1=dict(range=[min(polygon[:, 1]) - 5, max(polygon[:, 1]) + 5]),
        xaxis2=dict(range=[min(polygon[:, 0]) - 5, max(polygon[:, 0]) + 5]),
        yaxis2=dict(range=[min(polygon[:, 1]) - 5, max(polygon[:, 1]) + 5]),
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