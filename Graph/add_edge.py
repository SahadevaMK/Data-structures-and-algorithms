def addEdge(self,vertex1,vertex2):
        if vertex1 in self.graphDict.keys() and  vertex2 in self.graphDict.keys():
            self.graphDict[vertex1].append(vertex2)
            self.graphDict[vertex2].append(vertex1)
            return True
        return False
