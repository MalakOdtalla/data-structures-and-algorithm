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

    assert graph.get_nodes() == ['a','b']

# All appropriate neighbors can be retrieved from the graph



# Neighbors are returned with the weight between nodes included


# The proper size is returned, representing the number of nodes in the graph
def test_get_size():
    graph = Graph()
    a= graph.add_node('a')
    b = graph.add_node('b')

    assert graph.size() == 2

# A graph with only one node and edge can be properly returned


# An empty graph properly returns null

def test_empty_graph():
    graph = Graph()
    assert graph.get_nodes() == []




