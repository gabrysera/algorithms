from __future__ import annotations
from src.algorithms.fordFulkerson import ford_fulkerson
from src.data_structures.graph import *

def main():
    nodes = [Node("v1"), Node("v2"), Node("v3"), Node("v4")]
    source = Node("s")
    sink = Node("t")

    edges = [Edge(source, nodes[0], 11, 16), Edge(source, nodes[1],8,13), Edge(nodes[2],sink,15,20),
    Edge(nodes[3],sink,4,4), Edge(nodes[0],nodes[2],12,12), Edge(nodes[1],nodes[0],1,4), 
    Edge(nodes[1],nodes[3],11,14), Edge(nodes[3],nodes[2],7,7), Edge(nodes[2],nodes[1],4,9)]

    g = Graph(nodes ,edges)
    _, _, flow = ford_fulkerson(g, source, sink)
    print(flow)
    return


if __name__ == "__main__":
    main()