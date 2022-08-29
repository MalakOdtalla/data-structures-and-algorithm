from collections import deque
from stack_and_queue.stack_and_queue.Stack import Stack


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


class Vertex:
    def __init__(self, value):
        """
        Node/vertex constructor
        """
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])

    def breadth_first(self, Node):
        result = []
        visted = set()
        q = Queue()

        q.enqueue(Node)
        visted.add(Node)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result

    def Depth_first(self,starting_vertex):

        vertices = []
        depth = Stack()

        if starting_vertex not in self.__adj_list:
            return "error"

        depth.push(starting_vertex)

        while not depth.is_empty():
            top_vertex = depth.pop()
            vertices.append(top_vertex.value)
            top_node_neighbors = self.get_neighbors(top_vertex)

            for neighbor in top_node_neighbors[::-1]:
                if  neighbor[0] not in visited:
                    top_vertex.visited = True
                    neighbor[0].visited = True

                    depth.push(neighbor[0])

        for node in self.__adj_list:
            node.visited = False

        return vertices






if __name__ == "__main__":
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.add_edge(a, e)
    g.add_edge(e, a)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    print(g.Depth_first(b))
