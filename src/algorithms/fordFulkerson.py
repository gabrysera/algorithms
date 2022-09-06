from data_structures.graph import *
from data_structures.tree import Tree
from depthFirstSearch import depth_first_search_for_augmented_path

def residual_network(G:Graph) -> Graph:
    edges = G.E
    residual_G = Graph(G.V, list(map(lambda e: Edge(e.x, e.y, residual_capacity=e.capacity - e.flow), edges)) + 
    (list(map(lambda e: Edge(e.y, e.x, residual_capacity = e.flow), edges))))
    return residual_G

#given the residual graph return augmenting path and residual capacity
def augmenting_path(G:Graph, source:Node, sink:Node) -> tuple[list[Edge], int]:
    return depth_first_search_for_augmented_path(G, source, sink)

#take a graph, the source, the sink, and then return the graph with the values of flow such that we have a maximum
# flow and the min cut of this new graph 
def ford_fulkerson(G:Graph, s:Node, t:Node) -> tuple[Graph, Bipartition]:
    #set flow = 0 for all the edges 
    #iteratively increase flow by augmenting path
    #stop when augmenting path is empty
    return 
