from GraphAdjList import Graph, Vertex

def ShortestPath(G: Graph, src: Vertex, dest: Vertex):
    """
    returns the shortest path (min number of edges required) from src to dest vertex 
    G: un-directed graph with no weights
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    queue = []
    src.setDistance(0)
    queue.append(src)

    while queue:
        v = queue.pop(0)
        if not v.isVisited():
            G[v.getLabel()].visit()
            for nbr in v.getConnections():
                if not G[nbr].isVisited():
                    queue.append(G[nbr])
                    G[nbr].setDistance(v.getDistance() + 1)
    
    return -1 if G[dest.getLabel()].getDistance() == float("-inf") else G[dest.getLabel()].getDistance() 


def ShortestPathTree(G: Graph, src: Vertex):
    """
    Construct a shortest path tree of the give graph starting from src vertex 
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    pass

def TraverseShortestPathTree(G: Graph):
    """
    Traverse the shortest path tree and returns the list of visited element in particular order
    Input: G should have already computed Shortest path tree, pre should be set already.
    TimeComplexity: O(V)
    SpaceComplexity: O(1)
    """
    pass

def main():
    vertices, edges = map(int, input().split(" "))
    G = Graph()
    for v in range(vertices):
        G.addVertex(v+1)
    
    for _ in range(edges):
        u, v = map(int, input().split(" "))
        G.addEdge(u,v,False)
    
    src, dest = map(int, input().split(" "))
    print(ShortestPath(G,G[src], G[dest]))

if __name__ == "__main__":
    main()
