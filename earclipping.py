import numpy as np

def ear_clipping(polygon):
    """
    Triangulate a given polygon.

    Parameters:
    polygon (numpy.ndarray): An array of shape (n, 2) where n is the number of vertices of the polygon.

    Returns:
    tuple: A tuple containing:
        - triangles (list): A list of triangles, each triangle is a list of 4 points (the last point is the same as the first).
        - frames (list): A list of "frames", each frame is a tuple of two numpy arrays of shape (n,) representing the x and y coordinates of the polygon, less the points that have been removed.
    """
    def is_point_inside_triangle(p, p0, p1, p2):
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
        b1 = sign(p, p0, p1) <= 0.0
        b2 = sign(p, p1, p2) <= 0.0
        b3 = sign(p, p2, p0) <= 0.0
        return ((b1 == b2) and (b2 == b3))
    
    def is_turn_left(p0, p1, p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) > 0
    
    def is_ear(polygon, i):
        if not is_turn_left(polygon[i-1], polygon[i], polygon[(i+1)%len(polygon)]):
            return False
        p0 = polygon[i-1]
        p1 = polygon[i]
        p2 = polygon[(i+1)%len(polygon)]
        for j in range(len(polygon)):
            if j == i or j == i-1:
                continue
            if is_point_inside_triangle(polygon[j], p0, p1, p2):
                return False
        return True
    
    def remove_ear(polygon, i):
        return np.delete(polygon, i, axis=0)
    

    triangles = []
    frames = []
    while(len(polygon) > 3):
        for i in range(len(polygon)):
            if is_ear(polygon, i):
                triangles.append([polygon[i-1], polygon[i], polygon[(i+1)%len(polygon)], polygon[i-1]])
                frames += [(polygon[:,0], polygon[:,1])]
                polygon = remove_ear(polygon, i)
                break
    

    return triangles,frames