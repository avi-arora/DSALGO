from GraphAdjList import Graph, Vertex


def HasCycle(G: Graph):
    """
    Returns 1 if graph G contains a cycle else returns 0
    TimeComplexity: 
    SpaceComplexity: 
    """
    pass

def HasCycleBruteForce(G: Graph):
    
    


def main():
    #take user input
    totalVertices, totalEdges = map(int, input().split(" "))
    G = Graph()

    #populate vertices 
    for vertex in range(1, totalVertices+1):
        G.addVertex(vertex)

    #populate edges
    for _ in range(totalEdges):
        fromLabel, toLabel = map(int, input().split(" "))
        G.addEdge(fromLabel, toLabel, True)
    
    print(HasCycle(G))





if __name__ == "__main__":
    main()