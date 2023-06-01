class Node:
    def __init__(self,data):
        self.data = data
        self.nextRef = None
        self.prevRef = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head==None:
            print ('ll empty')
        else:
            n = self.head
            while(n!=None):
                print (n.data)
                n=n.nextRef
                


    def Insetbegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nextRef = self.head
            self.head.prevRef = new_node
            self.head = new_node
    
    def InsetEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n=self.head
            while(n.nextRef!=None):
                n=n.nextRef
            new_node.prevRef = n.nextRef
            n.nextRef = new_node
            new_node.prevRef = None



dll = doublyLinkedList()
dll.Insetbegin(20)
dll.Insetbegin(30)
dll.Insetbegin(500)
dll.InsetEnd(900)

dll.display()
