class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularSingleLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head

    def display(self):
        if not self.head:
            return
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
            if current==self.head:
                break

cll=CircularSingleLinkedList()
cll.append(8)
cll.append(10)
cll.append(12)
cll.append(13)
cll.append(9)
cll.display()
