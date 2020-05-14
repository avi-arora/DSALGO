"""

This file contains various combination of DFS (depth search algorithm)
with sources and time complexity.

"""
from GraphAdjList import *

def DFSAdjList(G: Graph):
    """
    Computes and return list of labels while traversing graph using DFS
    TimeComplexity: O(V + E) : why? give proof
    SpaceComplexity: O(1)
    """
    #utility for recursive computation of path
    def DFSUtility(vertex : Vertex, path):
        """
        Takes a Vertex, Recursive traverse it's neighbors
        """
        if not vertex.isVisited():
            vertex.visit()
            path.append(vertex.getLabel())
        for neighbor in vertex.getConnections():
            if not G.graph[neighbor].isVisited():
                DFSUtility(G.graph[neighbor],path)
    #list to store label in traversal order
    dfsPath = []
    for vertex in G.getVertices():
        DFSUtility(G.graph[vertex], dfsPath)

    return dfsPath

  
        



if __name__ == '__main__':
    print(DFSAdjList(SampleGraph_1()))