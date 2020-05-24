from GraphAdjList import Graph, Vertex

def ShortestPath(G: Graph, src: Vertex, dest: Vertex):
    """
    returns the shortest path (min number of edges required) from src to dest vertex
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    pass

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
    
    src, dest = map(int, input().split(" "))

    print(ShortestPath(G,G[src], G[dest]))

if __name__ == "__main__":
    main()
