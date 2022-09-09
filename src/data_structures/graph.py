from __future__ import annotations

class Node:
    def __init__(self, id, visited:bool = False):
        self.id = id   
        self.ingoing_edges = []
        self.outgoing_edges = []
        self.visited = visited


    #maybe for these 2 functions make such that current node is always first in the edges in the list
    def add_ingoing_edge(self, edge):
        self.ingoing_edges.append(edge)

    def add_outgoing_edge(self, edge):
        self.outgoing_edges.append(edge)


class Edge:
    def __init__(self, x:Node, y:Node, flow:int = 0, capacity:int = 0, residual_capacity = 0):
        assert not (capacity < flow), f"flow cannot be bigger than capacity for edge {x.id,y.id}, flow={flow}, capacity={capacity}"

        self.x = x
        self.y = y
        self.edge = (x,y)
        self.capacity = capacity
        self.flow = flow
        self.residual_capacity = residual_capacity
        x.add_outgoing_edge(self)
        y.add_ingoing_edge(self)
        
class Graph:
    
    def __init__(self, V:list[Node],  E:list[Edge]):
        def illegal_edges() -> bool:
            for e in E:
                if e.x not in V or e.y not in V:
                    return False
            return True

        assert not illegal_edges(), "some of these edges contains vertex that are not in the graph!!"
        
        self.E = E
        self.V = V
        self.dictE = {}
        for e in E:
            self.dictE[(e.x.id,e.y.id)] = e
        
    def add_edge(self, e:Edge):
        self.E.append(e)
        self.dictE[(e.x.id, e.y.id)] = e

    def get_edge(self, id_x, id_y):
        return self.dictE.get((id_x,id_y))

class Bipartition:

    def __init__(self, G:Graph, S:list[Node], T:list[Node]):
        self.G = G
        self.S = S
        self.T = T