import unittest
from simple_graph import SimpleGraph, Vertex


class TestSimpleGraph(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(5)
        for i in range(5):
            self.graph.AddVertex(i)

    def test_add_vertex(self):
        self.assertEqual(self.graph.vertex[0].Value, 0)
        self.assertEqual(self.graph.vertex[1].Value, 1)
        self.assertEqual(self.graph.vertex[2].Value, 2)
        self.assertEqual(self.graph.vertex[3].Value, 3)
        self.assertEqual(self.graph.vertex[4].Value, 4)

    def test_add_edge(self):
        self.graph.AddEdge(0, 1)
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(1, 0))

    def test_remove_edge(self):
        self.graph.AddEdge(0, 1)
        self.graph.RemoveEdge(0, 1)
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(1, 0))

    def test_remove_vertex(self):
        self.graph.RemoveVertex(0)
        self.assertIsNone(self.graph.vertex[0])
        for i in range(5):
            self.assertFalse(self.graph.IsEdge(0, i))

    def test_depth_first_search_path_exists(self):
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual([v.Value for v in path], [0, 1, 2, 3, 4])

    def test_depth_first_search_no_path(self):
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [])

    def test_depth_first_search_same_node(self):
        path = self.graph.DepthFirstSearch(0, 0)
        self.assertEqual([v.Value for v in path], [0])