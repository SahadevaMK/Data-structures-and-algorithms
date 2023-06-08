def deleteEnd(self):
        if self.head == None:
            print('ll empty nothing to delete')
            return
        if self.head.nextRef == None:
            self.head = None
            print('only one node is present in ll')
        else:
            n=self.head
            while(n.nextRef != None):
                n=n.nextRef
            n.prevRef.nextRef = None
