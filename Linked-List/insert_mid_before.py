
    def insertBeforeNode(self,data,x):
        # n=self.head
        if self.head == None:
            print('linked list is empty')
            return
        if (self.head.data == x):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while (n.ref != None):
            if (n.ref.data == x):
                break
            n=n.ref
        if n == None:
            print('linked List is empty')
        else:
            new_node = Node(data)
            new_node.ref =n.ref
            n.ref = new_node
