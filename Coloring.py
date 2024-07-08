def share_face(triangle1, triangle2):
    shared_point_counter = 0
    for point_1 in triangle1[:3]:
      for point_2 in triangle2[:3]:
            if ((point_1[0] == point_2[0]) and (point_1[1] == point_2[1])):
              shared_point_counter += 1
    if shared_point_counter >= 2:
      return True

    return False

class Coloring:
  def __init__(self, polygon):
    """
    Parameters:
      polygon (Polygon): The polygon to be colored.
    """
    self.polygon = polygon
    self.triangles = polygon.get_triangles()
    self.vertex_list = polygon.get_vertices()
    self.dual_graph_vertex = [[i,0] for i in range(len(self.triangles))]
    self.dual_graph_adj_list = [[] for i in range(len(self.triangles))]
    self.counter = 0
    for i in range(len(self.triangles)):
      for j in range(i, len(self.triangles)):
        if i == j:
          continue
        if share_face(self.triangles[i], self.triangles[j]):
          self.dual_graph_adj_list[i].append(j)
          self.dual_graph_adj_list[j].append(i)
    self.colored_vertex_list = []
    for i in range(len(self.vertex_list)):
      vertex_colored = [self.vertex_list[i], 'none']
      self.colored_vertex_list.append(vertex_colored)
    
    self.DFS()
  
  def point_index(self, point):
    for i in range(len(self.vertex_list)):
      if self.vertex_list[i][0] == point[0] and self.vertex_list[i][1] == point[1]:
        return i
    return -1

  def get_dual_graph_vertex(self):
    return self.dual_graph_vertex
  
  def get_dual_graph_adj_list(self):
    return self.dual_graph_adj_list
  
  def get_colored_vertex_list(self):
    return self.colored_vertex_list
  
  def DFS(self):
    for vertex_u in self.dual_graph_vertex:
      if vertex_u[1] == 0:
        self.DFS_procedure(vertex_u)
    return 0

  def DFS_procedure(self, v_u):
    self.counter += 1
    v_u[1] = self.counter #triangulo v_u visitado

    triangulo = self.triangles[v_u[0]]
    colors = [1, 2, 3]


    for i in range(len(triangulo[:3])):
      color = self.colored_vertex_list[self.point_index(triangulo[i])][1]

      if color == 'none': #o ponto i do triangulo não tem cor, simplesmente ignora.
        continue
      else:
        #print(f'removendo {color}')
        colors.remove(color)

    if len(colors) != 0: #falta colorir o triangulo com algumas cores.
      for i in range(len(triangulo[:3])):
        if self.colored_vertex_list[self.point_index(triangulo[i])][1] == 'none':
          self.colored_vertex_list[self.point_index(triangulo[i])][1] = colors.pop(0)

    for vertex_v in self.dual_graph_adj_list[v_u[0]]:
      if self.dual_graph_vertex[vertex_v][1] == 0:
        self.DFS_procedure(self.dual_graph_vertex[vertex_v])

    return 0