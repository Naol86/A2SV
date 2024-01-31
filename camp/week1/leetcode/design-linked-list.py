class double:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.pre = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = double()
        self.tail = double()
        self.head.next = self.tail
        self.tail.pre = self.head
        # self.tra(self.head)

    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while i <= index and current:
            current = current.next
            i += 1
        if current is None:
            return -1
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = double(val)
        new_node.pre = self.head
        new_node.next = self.head.next
        self.head.next.pre = new_node
        self.head.next = new_node

        # self.tra(self.head)

    def addAtTail(self, val: int) -> None:
        new_node = double(val)
        new_node.next = self.tail
        new_node.pre = self.tail.pre
        self.tail.pre.next = new_node
        self.tail.pre = new_node

        # self.tra(self.head)

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = double(val)
        current = self.head
        i = 0
        while i <= index and current:
            current = current.next
            i += 1
        if current == None:
            return
        new_node.next = current
        new_node.pre = current.pre
        current.pre.next = new_node
        current.pre = new_node

        # self.tra(self.head)

    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        i = 0
        while i <= index and current:
            current = current.next
            i += 1
        if current is None or current is self.tail:
            return 
        current.next.pre = current.pre
        current.pre.next = current.next

        # self.tra(self.head)
    
    def tra(self, head):
        while head:
            print(head.val, "------>",end=' ')
            head = head.next
        print("done")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)