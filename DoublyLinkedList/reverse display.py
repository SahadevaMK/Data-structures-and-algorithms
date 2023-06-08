def reverseDisplay(self):
        if self.head == None:
            print('ll empty')
        else:
            n= self.head
            while(n.nextRef!=None):
                n= n.nextRef
            while(n!=None):
                print(n.data)
                n= n.prevRef
