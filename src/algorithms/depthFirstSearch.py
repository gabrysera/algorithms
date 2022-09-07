from data_structures.graph import *
from data_structures.tree import Tree

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


def depth_first_search_for_augmented_path(G:Graph, source:Node, sink:Node) -> tuple[Tree, bool]:
    tree = Tree(source)
    path = [source]
    exist_augmented_path = True
    for node in G.V:
        node.visisted = False
    dfs(source)
    def dfs(u:Node):
        u.visited = True
        for (u, node) in u.outgoing_edges:
            if node.visited == False:
                path.append(node)
                tree.add_child(u,node)
                if node.id == sink.id:
                    return path
                dfs(node)
        path.pop()
    if path[-1].id != sink.id:
        exist_augmented_path = False
    return (path, exist_augmented_path)