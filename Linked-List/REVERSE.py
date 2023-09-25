def reverse(self):
        prev = None
        curNode = self.head
        nextNode = self.head
        
        while(nextNode!=None):
            nextNode=nextNode.ref
            curNode.ref=prev
            prev = curNode
            curNode=nextNode
            
        self.head=prev
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.ref
