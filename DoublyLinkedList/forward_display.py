def ForwardDisplay(self):
        if self.head == None:
            print('ll empty')
        else:
            n= self.head
            while(n!=None):
                print(n.data)
                n=n.nextRef
