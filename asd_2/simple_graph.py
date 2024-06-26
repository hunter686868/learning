class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # со значением value
        # в свободное место массива vertex
        if None not in self.vertex:
            return False
        new_vertex = Vertex(v)
        index = 0
        while index < len(self.vertex) and self.vertex[index] is not None:
            index += 1

        self.vertex[index] = new_vertex
        return True
        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if v < 0 or v >= self.max_vertex or self.vertex[v] is None:
            return False
        self.vertex[v] = None
        for index in range(len(self.vertex)):
            self.m_adjacency[index][v] = 0
            self.m_adjacency[v][index] = 0
        return True

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            return False
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False

        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if v1 < 0 or v1 >= self.max_vertex or v2 < 0 or v2 >= self.max_vertex:
            return False
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return False

        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return True

