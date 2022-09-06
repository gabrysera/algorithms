from graph import *

class Tree:
    def __init__(self, root:Node, edges:list[Edge]=[]):
        self.root = root
        self.edges = edges

    def add_child(self, node_x:Node, node_y:Node):
        self.edges.append(Edge(node_x, node_y))