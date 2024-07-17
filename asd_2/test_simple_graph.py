import unittest
from simple_graph import SimpleGraph, Vertex


class TestSimpleGraph(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(5)

    def test_add_vertex(self):
        self.assertTrue(self.graph.AddVertex(1))
        self.assertEqual(self.graph.vertex[0].Value, 1)
        self.assertTrue(self.graph.AddVertex(2))
        self.assertEqual(self.graph.vertex[1].Value, 2)
        self.assertTrue(self.graph.AddVertex(3))

    def test_remove_vertex(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.assertTrue(self.graph.RemoveVertex(0))
        self.assertIsNone(self.graph.vertex[0])
        self.assertTrue(self.graph.RemoveVertex(1))
        self.assertIsNone(self.graph.vertex[1])
        self.assertFalse(self.graph.RemoveVertex(2))

    def test_add_remove_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.assertTrue(self.graph.AddEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.RemoveEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(0, 1))

    def test_depth_first_search(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        path = self.graph.DepthFirstSearch(0, 2)
        self.assertEqual([v.Value for v in path], [1, 2, 3])

    def test_breadth_first_search(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        path = self.graph.BreadthFirstSearch(0, 2)
        self.assertEqual([v.Value for v in path], [1, 2, 3])

    def test_weak_vertices(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 0)
        self.graph.AddEdge(3, 1)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [4])
