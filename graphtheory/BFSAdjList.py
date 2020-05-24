from GraphAdjList import Graph, Vertex

def BFSWithoutDistance(G: Graph):
    """
    Returns a list of vertices (labels) traversed in BFS order
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    visited, queue = [], []
    queue.append(G.getVertex(list(G.getVertices())[0]))
    while queue: 
        elem = queue.pop(0)
        if not elem.isVisited():
            elem.visit()
            visited.append(elem.getLabel())
            for nbr in elem.getConnections():
                if not G[nbr].isVisited():
                    queue.append(G[nbr])
    
    return visited

def BFSWithDistance(G: Graph, srcVertex: Vertex):
    """
    Returns a list of vertices (labels) traverse in BFS Order
    Also computes the distance between the source vertices to the other vertices 
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    queue, visited = [], []
    srcVertex.distance = 0
    srcVertex.visit()
    queue.append(srcVertex)

    while queue:
        v = queue.pop(0)
        visited.append(v.getLabel())
        for nbr in v.getConnections():
            if not G[nbr].isVisited():
                G[nbr].visit()
                G[nbr].setDistance(v.getDistance() + 1)
                queue.append(G[nbr])
    
    return visited



def main():
    totalVertex, totalEdges = map(int, input().split(" "))
    G = Graph()
    #fill vertices 
    for v in range(totalVertex):
        G.addVertex(v+1)
    
    #take input
    for _ in range(totalEdges):
        v, u = map(int, input().split(" "))
        G.addEdge(v,u)
    
    startingVertex = G[list(G.getVertices())[0]]
    print(BFSWithDistance(G, G[startingVertex])


if __name__ == "__main__":
    main()
    
    


    
