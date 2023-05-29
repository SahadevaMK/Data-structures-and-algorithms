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
