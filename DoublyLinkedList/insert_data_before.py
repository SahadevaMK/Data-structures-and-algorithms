def insertBefore(self, data,x):
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
                new_node.nextRef = n
                new_node.prevRef = n.prevRef
                if n.prevRef != None:
                    n.prevRef.nextRef = new_node
                n.prevRef = new_node
