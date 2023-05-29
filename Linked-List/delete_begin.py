def deleteBegin(self):
        if self.head == None:
            print('linked List is empty')
        else:
            self.head = self.head.ref
