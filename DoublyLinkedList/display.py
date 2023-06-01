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
