class Node:
    def __init__(self, id, ingoing_edges = [], outgoing_edges = [], visited:bool = False):
        self.id = id   
        self.ingoing_edges = ingoing_edges
        self.outgoing_edges = outgoing_edges
        self.visisted = visited


    #maybe for these 2 functions make such that current node is always first in the edges in the list
    def add_ingoing_edge(self, edge):
        self.ingoing_edges.append(edge)

    def add_outgoing_edge(self, edge):
        self.outgoing_edges.append(edge)




class Edge:
    def __init__(self, x:Node, y:Node, flow:int = 0, capacity:int = 0, residual_capacity = 0):
        if capacity < flow:
            raise ValueError(f"flow cannot be bigger than capacity for edge {x,y}")
        self.edge = (x,y)
        self.capacity = capacity
        self.flow = flow
        self.residual_capacity = residual_capacity
        x.add_outgoing_edge(self.edge)
        y.add_ingoing_edge(self.edge)
        
class Graph:
    
    def __init__(self,V:list[Node],  E:list[Edge]):
        def illegal_edges() -> bool:
            for e in E:
                if e[0] not in V or e[1] not in V:
                    return False
            return True

        if illegal_edges():
            raise ValueError(f"some of these edges contains vertex that are not in the graph!!")
        self.E = E
        self.V = V

class Bipartition:

    def __init__(self, G:Graph, S:list[Node], T:list[Node]):
        self.G = G
        self.S = S
        self.T = T