class double:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.nodes = {}
        self.MAX = capacity
        self.size = 0
        self.tail = double()
        self.head = double()

        self.head.next = self.tail
        self.tail.prev = self.head
        # self.tra(self.head)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        temp = self.nodes[key]
        self.remove(temp)
        self.put(key, temp.val)
        # self.tra(self.head)
        return temp.val
        
    def put(self, key: int, value: int) -> None:
        new_node = double(value, key, self.tail, self.tail.prev)
            
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        if key in self.nodes:
            self.remove(self.nodes[key])
        self.size += 1
        self.nodes[key] = new_node
        if self.size > self.MAX:
            self.remove(self.head.next)
        # print(self.size)
        # self.tra(self.head)

    def remove(self, node):
        self.size -= 1
        # print(self.nodes,node.key)
        self.nodes.pop(node.key)
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return 
        
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def tra(self, node):
        while node:
            print(node.key,node.val,"-------> ",end=" ")
            node = node.next
        print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)