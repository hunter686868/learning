import unittest
from simple_graph import SimpleGraph, Vertex


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

    def test_add_vertex(self):
        self.assertTrue(self.graph.AddVertex(1))
        self.assertIsNotNone(self.graph.vertex[0])
        self.assertEqual(self.graph.vertex[0].Value, 1)

    def test_add_multiple_vertices(self):
        self.assertTrue(self.graph.AddVertex(1))
        self.assertTrue(self.graph.AddVertex(2))
        self.assertIsNotNone(self.graph.vertex[1])
        self.assertEqual(self.graph.vertex[1].Value, 2)

    def test_add_vertex_no_free_slot(self):
        for i in range(5):
            self.assertTrue(self.graph.AddVertex(i))
        self.assertFalse(self.graph.AddVertex(5))

    def test_remove_vertex(self):
        self.graph.AddVertex(1)
        self.assertTrue(self.graph.RemoveVertex(0))
        self.assertIsNone(self.graph.vertex[0])
        for i in range(self.graph.max_vertex):
            self.assertEqual(self.graph.m_adjacency[0][i], 0)
            self.assertEqual(self.graph.m_adjacency[i][0], 0)

    def test_remove_vertex_invalid_index(self):
        self.assertFalse(self.graph.RemoveVertex(-1))
        self.assertFalse(self.graph.RemoveVertex(5))

    def test_add_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.assertTrue(self.graph.AddEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(1, 0))

    def test_add_edge_invalid_vertices(self):
        self.assertFalse(self.graph.AddEdge(0, 1))

    def test_remove_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddEdge(0, 1)
        self.assertTrue(self.graph.RemoveEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(1, 0))

    def test_remove_edge_invalid_vertices(self):
        self.assertFalse(self.graph.RemoveEdge(0, 1))

    def test_is_edge_invalid_vertices(self):
        self.assertFalse(self.graph.IsEdge(0, 5))
        self.assertFalse(self.graph.IsEdge(5, 0))
