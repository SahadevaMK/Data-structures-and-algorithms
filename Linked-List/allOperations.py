class Node:
    def __init__(self,data):
        self.data = data;
        self.ref = None;
        
        
class linkedList:
    def __init__(self):
        self.head = None;
    
    
    def display(self):
        n = self.head;
        if (self.head == None):
            print('ll empty');
        else:
            while(n!=None):
                print(n.data);
                n = n.ref;
        
    def insetBegin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def insertEnd(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            n = self.head
            while(n.ref!=None):
                n=n.ref
            n.ref = new_node
            new_node.ref = None
    
    def insertAfter(self,data,x):
        n = self.head
        while(n!=None):
            if (n.data == x):
                break
            n=n.ref
        if (n == None):
            print('NOT S')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insertBefore(self,data,x):
        n = self.head
        if (n.data == x):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        while(n!=None):
            if (n.ref.data == x):
                break
            n = n.ref
        if (n == None):
            print('node not present')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def deleteBegin(self):
        if self.head == None:
            print('linked List is empty')
        else:
            self.head = self.head.ref
    
    def deleteEnd(self):
        n =self.head
        while(n.ref.ref!=None):
            n = n.ref
        n.ref= None
        
    def deleteByValue(self, x):
        if (self.head == None):
            print('linked list is empty so no elements cant be deleted')
            return
        if (self.head.data == x):
            self.head = self.head.ref  
            return
        n = self.head
        while(n.ref != None):
            if (x == n.ref.data): 
                break
            n = n.ref
        if (n.ref == None):
            print('no node of that name x to be deleted')
        else:
            n.ref = n.ref.ref
            
    def MinMax(self):
        mini = self.head.data
        maxi = self.head.data
        n = self.head
        while(n!=None):
            if (n.data > maxi):
                maxi = n.data
            elif(n.data<mini):
                mini=n.data
            n = n.ref
        print(maxi)
        print(mini)
    
    def reverse(self):
        prev = None
        curNode = self.head
        nextNode = self.head
        
        while(nextNode!=None):
            nextNode=nextNode.ref
            curNode.ref=prev
            prev = curNode
            curNode=nextNode
            
        self.head=prev
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.ref
        
            

        
        

sll = linkedList()
sll.insetBegin(5)
sll.insetBegin(10)
sll.insetBegin(25)
sll.insertEnd(100)
sll.display()
print("---------")
sll.reverse()
