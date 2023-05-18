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
    
    
    
    def add_middle_after(self,data,x):
        n = self.head
        while (n.data!=x):
            break
        else:
            n=n.ref
        if n==None:
            print('the given node is not present in linkedList')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

linkedList = SingleLinkedList()

linkedList.add_begin(25)
linkedList.add_begin(35)
linkedList.add_end(100)
linkedList.add_middle_after(69,35)
linkedList.Display()
