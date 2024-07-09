import unittest
from simple_graph import SimpleGraph, Vertex


class TestSimpleGraph(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(5)
        self.graph.AddVertex(0)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)

    def test_add_vertex(self):
        self.assertFalse(self.graph.AddVertex(5))  # Adding beyond the initial size should fail
        self.assertTrue(self.graph.RemoveVertex(2))  # Removing vertex should succeed
        self.assertTrue(self.graph.AddVertex(2))  # Adding a vertex after removal should succeed

    def test_remove_vertex(self):
        self.assertTrue(self.graph.RemoveVertex(1))
        self.assertIsNone(self.graph.vertex[1])
        for i in range(self.graph.max_vertex):
            self.assertEqual(self.graph.m_adjacency[1][i], 0)
            self.assertEqual(self.graph.m_adjacency[i][1], 0)

    def test_add_edge(self):
        self.assertFalse(self.graph.AddEdge(0, 5))  # Adding an edge to a non-existent vertex should fail
        self.assertTrue(self.graph.AddEdge(0, 4))
        self.assertTrue(self.graph.IsEdge(0, 4))

    def test_remove_edge(self):
        self.assertTrue(self.graph.RemoveEdge(1, 2))
        self.assertFalse(self.graph.IsEdge(1, 2))

    def test_depth_first_search(self):
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [0, 1, 2, 3, 4])

        self.graph.RemoveEdge(2, 3)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [])

        self.graph.AddEdge(1, 3)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [0, 1, 3, 4])
