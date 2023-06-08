def insertEmpty(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('ll not empty')
