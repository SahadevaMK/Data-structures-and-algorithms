class Node:
    def __init__(self,data):
        self.data = data
        self.ref =None
        
class SingleLinkedList:
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
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head=new_node

linkedList = SingleLinkedList()

linkedList.add_begin(25)
linkedList.add_begin(35)
linkedList.Display()
