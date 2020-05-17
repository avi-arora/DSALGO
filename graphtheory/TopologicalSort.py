from GraphAdjList import Graph, Vertex


def TopologicalSort(G: Graph):
    """
    This function will return list of label sorted in topological ordering. 
    Uses slight modification of DFS
    TimeComplexity: For Original Topological Sorting O(|v|^2) for optimized version: O(V + E)
    SpaceComplexity: 
    """
    sorted = []
    def Util(v: Vertex):
        v.visit()
        for nbr in v.getConnections():
            if not G[nbr].isVisited():
                Util(G[nbr])
        #sink of a graph.
        sorted.append(v.getLabel())
    
    for vertex in G.getVertices():
        if not G[vertex].isVisited():
            Util(G[vertex])
    
    return sorted[::-1]
        



def TopologicalSortBruteForce(G: Graph):
    """
    un-optimized version of topological sorting
    """
    sorted = []
    for vertex in G.getVertices():
        pass
         

if __name__ == "__main__":
    G = Graph()
    G.addVertex("2")
    G.addVertex("3")
    G.addVertex("5")
    G.addVertex("7")
    G.addVertex("8")
    G.addVertex("9")
    G.addVertex("10")
    G.addVertex("11")

    G.addEdge("7","8",True)
    G.addEdge("7","11", True)
    G.addEdge("5","11", True)
    G.addEdge("3","8", True)
    G.addEdge("3","10", True)
    G.addEdge("11","9", True)
    G.addEdge("11","10", True)
    G.addEdge("8","9", True)
    G.addEdge("11","2", True)

    print(TopologicalSort(G)) 
    