def deleteBegin(self):
        if self.head == None:
            print('ll empty nothing to delete')
            return
        if self.head.nextRef == None:
            self.head = None
            print('only one node is present in ll')
        else:
            self.head = self.head.nextRef
            self.head.prevRef = None
