def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.graphDict.keys() and  vertex2 in self.graphDict.keys():
            try:
                self.graphDict[vertex1].remove(vertex2)
                self.graphDict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
