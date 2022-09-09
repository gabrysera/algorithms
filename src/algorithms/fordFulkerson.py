from __future__ import annotations
from ..data_structures.graph import *
from ..data_structures.tree import Tree
from .depthFirstSearch import depth_first_search_for_augmented_path

def residual_network(G:Graph) -> Graph:
    edges = G.E
    residual_G = Graph(G.V, list(map(lambda e: Edge(e.x, e.y, residual_capacity=e.capacity - e.flow), edges)) + 
    (list(map(lambda e: Edge(e.y, e.x, residual_capacity = e.flow), edges))))
    return residual_G

#given the residual graph return augmenting path and residual capacity
def augmenting_path(G:Graph, source:Node, sink:Node) -> tuple[list[Edge], bool]:
    return depth_first_search_for_augmented_path(G, source, sink)

#take a graph, the source, the sink, and then return the graph with the values of flow such that we have a maximum
# flow and the min cut of this new graph 
#seems to work but ugly code, its not efficient as it could be.
def ford_fulkerson(G:Graph, s:Node, t:Node) -> tuple[Graph, Bipartition, int]:
    #set flow = 0 for all the edges 
    for e in G.E:
        e.flow = 0
    
    finished = False
    #iteratively increase flow by augmenting path
    while(finished == False):
        G_augmented = residual_network(G)
        augm_path, finished = augmenting_path(G_augmented, s, t)
    
        if finished or len(augm_path) <= 1:
            break
        #take min in e in augm_path and then increase those same egdes in the real G
        min_increase = 1000000
        for e in augm_path:
            min_increase = min(min_increase, e.residual_capacity)
        for e in augm_path:
            edge = G.get_edge(e.x.id, e.y.id)
            edge.flow += min_increase
    flow = 0
    for e in t.ingoing_edges:
        flow += e.flow
    return (G, None, flow)
