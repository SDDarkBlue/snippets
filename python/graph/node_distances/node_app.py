import math

class App():
    def __init__(self):
        self.nodes = []
        self.next_node_id = 0

    def createNode(self, x=None, y=None):
        self.nodes.append(Node(x=x, y=y, id=self.next_node_id))
        self.next_node_id += 1

    def getNodes(self):
        return self.nodes

    def getDistances(self):
        result = []
        other_nodes = list(self.nodes)
        for node in self.nodes:
            other_nodes.remove(node)
            dists = node.getDistances(other_nodes)
            for dist in dists:
                result.append(dist)
        return result

class Node():
    def __init__(self, x=None, y=None, id=None):
        self.id = id
        self.x = x
        self.y = y

    def getXY(self):
        return [self.x, self.y]

    def get_id(self):
        return self.id

    def getDistances(self, nodes_list):
        result = []
        for node in nodes_list:
            x_dist = self.x - node.getXY()[0]
            y_dist = self.y - node.getXY()[1]
            dist = math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))
            result.append({'id': self.id, 'to_id': node.get_id(), 'dist': dist})
        return result

