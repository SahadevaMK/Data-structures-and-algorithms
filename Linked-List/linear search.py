def searching(self,x):
        if self.head == None:
            print('ll empty')
        else:
            n= self.head
            while(n!=None):
                if (n.data == x):
                    print('found')
                    break
                n=n.ref
            else:
                print ('data not found')
