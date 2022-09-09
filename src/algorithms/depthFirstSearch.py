from __future__ import annotations
from ..data_structures.graph import *
from ..data_structures.tree import Tree

def depth_first_search(G:Graph, v:Node) -> Tree:
    tree = Tree(v)
    for node in G.V:
        node.visisted = False
    def dfs(u):
        u.visited = True
        for (u, node) in u.add_outgoing_edge:
            if node.visited == False:
                tree.add_child(u,node)
                dfs(node)
    return tree


def depth_first_search_for_augmented_path(G:Graph, source:Node, sink:Node) -> tuple[list[Edge], bool]:
    path = []
    finished = False
    for node in G.V:
        node.visited = False

    def dfs(u:Node):
        u.visited = True
        for e in u.outgoing_edges:
            if e.y.visited == False and e.flow < e.capacity and (len(path) == 0 or path[-1].y.id != "t"): #and residual capacity > 0 ??    
                path.append(e)
                e.residual_capacity = e.capacity - e.flow
                G.add_edge(Edge(e.y,e.x,residual_capacity=e.capacity-e.residual_capacity))
                if e.y.id == sink.id:
                    return
                dfs(e.y)
        return 
    
    dfs(source)
    if len(path) != 0 and path[-1].y.id != sink.id:
        finished = True
    return (path, finished)