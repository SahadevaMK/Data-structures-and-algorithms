def insertAfterNode(self, data,x):
        n=self.head
        while n != None:
            if(x==n.data):
                break
            n = n.ref
        if n == None:
            print('node is not present')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
