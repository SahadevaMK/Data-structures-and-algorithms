class Graph:
    def __init__(self):
        self.graphDict = {}
    

    def addVertex(self,vertex):
        if vertex not in self.graphDict.keys():
            self.graphDict[vertex] = []
            return True
        return False
