def sumOfAllElemnets(self):
        sum1 = 0
        if self.head == None:
            print('ll empty sum = 0')
        else:
            n= self.head
            while(n!=None):
                sum1+=n.data
                n=n.ref
            print(sum1)
