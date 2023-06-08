def isSorted(self):
        x = -32768
        if (self.head == None):
            print('ll empty')
        else:
            n=self.head
            while(n!=None):
                if (n.data<x):
                    return False
                x=n.data
                n=n.ref
            return True
