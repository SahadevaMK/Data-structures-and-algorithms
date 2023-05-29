def deleteEnd(self):
        if (self.head ==None):
            print('linked List is empty so no elements cant be deleted')
        n=self.head
        while (n.ref.ref != None):
            n = n.ref
        n.ref = None
