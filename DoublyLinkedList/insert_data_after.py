def insertAfer(self,data,x):
        if self.head == None:
            print('given data is not present in linked list')
        else:
            n= self.head
            while(n!=None):
                if(n.data == x):
                    break
                n=n.nextRef
            if (n==None):
                print('')
            else:
                new_node = Node(data)
                new_node.nextRef = n.nextRef
                new_node.prevRef = n
                if n.nextRef != None:
                    n.nextRef.prevRef = new_node
                n.nextRef = new_node
