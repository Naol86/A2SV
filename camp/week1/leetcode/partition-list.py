# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def delete_node(self, node):
        temp = node.next
        node.next = node.next.next
        return temp

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.val < x:
            new_node = ListNode(head.val)
            new_node.next = self.partition(head.next,x)
            return new_node
        root = head
        insert_in = None
        current = head
        while current.next:
            if current.next.val < x:
                temp = self.delete_node(current)
                if not insert_in:
                    temp.next = root
                    root = temp
                    insert_in = temp
                else:
                    temp.next = insert_in.next
                    insert_in.next = temp
                    insert_in = temp
            else:
                current = current.next
        return root

        