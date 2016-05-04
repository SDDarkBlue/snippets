import unittest
import node_app

#@unittest.SkipTest
class TestNodeApp(unittest.TestCase):
    # unittest
    def test_getNrOfNodes(self):
        app = node_app.App()
        app.createNode(x=1, y=1)
        self.assertEqual(1, len(app.getNodes()))
        app.createNode(x=1, y=1)
        self.assertEqual(2, len(app.getNodes()))

    # e2e test
    #@unittest.SkipTest
    def test_distance_2_nodes(self):
        app = node_app.App()
        app.createNode(x=1, y=1)
        app.createNode(x=2, y=1)
        expected_distances = [{'id': 0, 'to_id': 1, 'dist': 1}]
        distances = app.getDistances()
        self.assertEqual(len(distances), 1)
        for i in range(1):
            for j in ['id', 'to_id', 'dist']:
                self.assertEqual(expected_distances[i][j], distances[i][j])

class TestNode(unittest.TestCase):
    def test_getSetXY(self):
        node = node_app.Node(x=1, y=1, id=0)
        self.assertEqual([1, 1], node.getXY())

    def test_get_id(self):
        node = node_app.Node(x=1, y=1, id=0)
        self.assertEqual(0, node.get_id())

    def test_getDistances(self):
        node0 = node_app.Node(x=1, y=1, id=0)
        node1 = node_app.Node(x=1, y=0, id=1)
        expected_result = [{'id': 0, 'to_id': 1, 'dist': 1}]
        result = node0.getDistances([node1])
        self.assertEqual(expected_result[0]['id'], result[0]['id'])
        self.assertEqual(expected_result[0]['to_id'], result[0]['to_id'])
        self.assertEqual(expected_result[0]['dist'], result[0]['dist'])
        self.assertEqual(node0.getDistances([]), [])

