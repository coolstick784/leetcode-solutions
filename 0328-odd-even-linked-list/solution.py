# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = None
        node = head
        ctr = 0
        while node:
            tail = node
            node = node.next
            ctr += 1
        node = head
        fin_ctr = 0

        while node and fin_ctr < ctr // 2:
            if node.next:
                tail.next = ListNode(node.next.val, None)
            else:
                tail.next = node.next
            tail = tail.next
            node.next = node.next.next
            node = node.next
          
            fin_ctr += 1


        return head
