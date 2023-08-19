class Graph:
    def __init__(self):
        self.graphDict = {}
    

    def addVertex(self,vertex):
        if vertex not in self.graphDict.keys():
            self.graphDict[vertex] = []
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.graphDict.keys() and  vertex2 in self.graphDict.keys():
            self.graphDict[vertex1].append(vertex2)
            self.graphDict[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.graphDict.keys() and  vertex2 in self.graphDict.keys():
            try:
                self.graphDict[vertex1].remove(vertex2)
                self.graphDict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex in self.graphDict.keys():
            for i in self.graphDict[vertex]:
                self.graphDict[i].remove(vertex)
            del self.graphDict[vertex]
            return True
        return False
    

    def PrintGraph(self):
        for vertex in self.graphDict:
            print(vertex , ':',self.graphDict[vertex])

graph = Graph()

graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('d')
graph.addVertex('c')
graph.addEdge('a','b')
graph.addEdge('a','c')
graph.addEdge('a','d')
graph.addEdge('b','c')
graph.addEdge('c','d')
graph.removeVertex('d')
graph.PrintGraph()
