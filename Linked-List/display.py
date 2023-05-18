class Node:
    def __init__(self,data):
        self.data = data
        self.ref =None
        
class SLL:
    def __init__(self):
        self.head=None
    
    def Display(self):
        if self.head is None:
            print('empty ll')
        else:
            temp = self.head
            while(temp is not None ):
              print(temp.data)
              temp = temp.ref
         
                
