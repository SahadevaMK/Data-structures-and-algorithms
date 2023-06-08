def findMaxMinElement(self):
        max = self.head.data
        min = self.head.data
        if self.head == None:
            print('empty')
        else:
            n= self.head
            while(n !=None):
                if (n.data > max):
                    max = n.data
                elif(n.data < min):
                    min = n.data
                n=n.ref
            print(max)
            print(min)
