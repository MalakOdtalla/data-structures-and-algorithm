from graph import Graph,Edge,Vertex


# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    vertex = graph.add_node('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()

    a = graph.add_node('a')
    b= graph.add_node('b')
    graph.add_edge(a, b)

#  retrieve all nodes from the graph
def test_retrieve_nodes():
    graph = Graph()

    graph.add_node('a')
    graph.add_node('b')
    actual=graph.get_nodes()

    assert actual == ['a','b']

# All appropriate neighbors can be retrieved from the graph

def test_retrieve_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')

    graph.add_edge(a, b)
    actual = len(graph.get_neighbors(a))
    expected = 1
    assert actual == expected

# Neighbors are returned with the weight between nodes included
def test_retrieve_neighbors_with_weight():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a , b , 2)
    graph.add_edge(a , c , 9)
    assert graph.get_neighbors(a) == [(b , 2) , (c , 9)]


# The proper size is returned, representing the number of nodes in the graph
def test_get_size():
    graph = Graph()
    a= graph.add_node('a')
    b = graph.add_node('b')

    assert graph.size() == 2

# A graph with only one node and edge can be properly returned
def test_graph_one_node():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a, a)
    assert graph.get_nodes() == [(a)]

# An empty graph properly returns null

def test_empty_graph():
    graph = Graph()
    assert graph.get_nodes() == []

def test_breadth_first_single_value():
  graph = Graph()
  a = graph.add_node('a')
  assert graph.breadth_first(a) == ['a']


def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    assert graph.breadth_first(a) == ['a']

