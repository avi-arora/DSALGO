class Vertex:
    def __init__(self, label):
        self.label, self.visited = label, False
        self.neighbors = []
        #stores pre and post visit values
        self.pre, self.post = 0, 0
    
    #to add a neighbor
    def addNeighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def getConnections(self):
        return self.neighbors
    
    def getVertexLabel(self):
        return self.label

    def visit(self):
        self.visited = True
    
    def preVisit(self, value):
        self.pre = value
    
    def postVisit(self, value):
        self.post = value

    def getPre(self):
        return self.pre
    
    def getPost(self):
        return self.post
    
    def isVisited(self):
        return self.visited

    def getLabel(self):
        return self.label
    
class Graph:
    def __init__(self):
        self.graph = {}
    
    def __getitem__(self,label):
        return self.graph[label]
    
    def totalVertices(self):
        return len(self.graph.keys())
    
    def addVertex(self, label):
        self.graph[label] = Vertex(label)
    
    def getVertices(self):
        return self.graph.keys()
    
    def getVertex(self,label):
        return self.graph[label]

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

def SampleGraph_1():
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')
    
    G.addEdge('a','b')
    G.addEdge('b','c')
    G.addEdge('c','d')
    G.addEdge('c','e')
    G.addEdge('f','e')
    G.addEdge('e','g')
    G.addEdge('e','h')
    G.addEdge('b','h')
    
    return G
    

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addEdge('a','b')
    G.addEdge('a','c')
    G.printGraph()
    print(G.getEdges())



        


