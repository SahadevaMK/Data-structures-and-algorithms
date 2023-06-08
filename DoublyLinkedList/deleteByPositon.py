def deleteByPositon(self,x):
        if self.head == None:
            print('ll empty nothing to delete')
            return
        if self.head.nextRef == None:
            self.head = None
        else:
            print('x is not  present in ll')
            return
        if (self.head.data == x):
            self.head = self.head.nextRef
            self.head.prevRef = None
            return
        n= self.head
        while(n.nextRef != None):
            if (n.data == x):
                break
            n=n.nextRef
        if n.nextRef != None:
            n.nextRef.prefRef = n.prefRef
            n.prefRef.nextRef = n.nextRef
        else:
            if n.data == x:
                n.prefRef.nextRef = None
            else:
                print('no such data in linked list')
