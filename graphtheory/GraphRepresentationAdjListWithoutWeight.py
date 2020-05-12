class Vertex:
    def __init__(self, label):
        self.label, self.visited = label, False
        self.neighbors = []
    
    #to add a neighbor
    def addNeighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def getConnections(self):
        return self.neighbors
    
    def getVertexLabel(self):
        return self.label

    def visited(self):
        self.visited = True
    
class Graph:
    def __init__(self):
        self.graph = {}
    
    def totalVertices(self):
        return len(self.graph.keys())
    
    def addVertex(self, label):
        self.graph[label] = Vertex(label)
    
    def getVertices(self):
        return self.graph.keys()

    def addEdge(self, fromLabel, toLabel,isDirected=False):
        """ This method also consider the edge cases
            if fromLabel and toLabel isn't a vertex yet, 
            it'll add them to vertex list
        """
        #handle corner cases listed in description
        if fromLabel not in self.getVertices():
            self.addVertex(fromLabel)
        if toLabel not in self.getVertices():
            self.addVertex(toLabel)
        #add the edge
        self.graph[fromLabel].addNeighbor(toLabel)
        #handle undirected graph case
        if not isDirected:
            self.graph[toLabel].addNeighbor(fromLabel)
    
    def getEdges(self):
        edges = []
        for u in self.getVertices():
            individual = []
            for e in self.graph[u].getConnections():
                individual.append([u,e])
            edges.append(individual)
        return edges

    def printGraph(self):
        for v in self.getVertices():
            print(v)
            print(self.graph[v].getConnections())

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addEdge('a','b')
    G.addEdge('a','c')
    G.printGraph()
    print(G.getEdges())

        


