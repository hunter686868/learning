class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]


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

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False
        stack = Stack()
        stack.push((VFrom, [VFrom]))

        while stack.size() > 0:
            current_index, current_path = stack.pop()
            current_vertex = self.vertex[current_index]

            if current_vertex.Hit is False:
                current_vertex.Hit = True

            if current_index == VTo:
                return [self.vertex[i] for i in current_path]

            for index in range(len(self.vertex)):
                if self.m_adjacency[current_index][index] == 1 and self.vertex[index].Hit is False:
                    stack.push((index, current_path + [index]))

        return []

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

        vertex_queue = Queue()
        vertex_queue.enqueue((VFrom, [VFrom]))

        while vertex_queue.size() > 0:
            current_index, current_path = vertex_queue.dequeue()
            current_vertex = self.vertex[current_index]

            if current_vertex.Hit is False:
                current_vertex.Hit = True

            if current_index == VTo:
                return [self.vertex[i] for i in current_path]

            for index in range(len(self.vertex)):
                if self.m_adjacency[current_index][index] == 1 and self.vertex[index].Hit is False:
                    vertex_queue.enqueue((index, current_path + [index]))

        return []

    def WeakVertices(self):
        # возвращает список узлов вне треугольников
        no_triangle_nodes = []
        for index in range(len(self.vertex)):
            if self.vertex[index] is not None and not self._is_triangle(index):
                no_triangle_nodes.append(self.vertex[index])
        return no_triangle_nodes

    def _is_triangle(self, node_index):
        neighbors = [i for i in range(len(self.vertex)) if self.m_adjacency[node_index][i] == 1]
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if self.m_adjacency[neighbors[i]][neighbors[j]] == 1:
                    return True
        return False

