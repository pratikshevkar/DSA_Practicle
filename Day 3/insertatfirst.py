class LinkList:
    def insert(self, new_node,pos):
        if(pos==1):
            new_node.next=self.head
            self.head = new_node
        else:
            p=1
            temp = self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1