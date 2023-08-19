def removeVertex(self,vertex):
        if vertex in self.graphDict.keys():
            for i in self.graphDict[vertex]:
                self.graphDict[i].remove(vertex)
            del self.graphDict[vertex]
            return True
        return False
