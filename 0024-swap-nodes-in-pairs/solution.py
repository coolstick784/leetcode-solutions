# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        while cur_node is not None and cur_node.next is not None:
            if cur_node == head:
                fol = cur_node.next
                cur_node.next = cur_node
                head = fol
                cur_node.next = head.next
                head.next = cur_node
                cur_node = head.next
            elif cur_node.next.next is not None and cur_node.next is not None:
                fol = cur_node.next.next
                prev = cur_node.next
                prev.next = fol.next
                fol.next = prev
                cur_node.next = fol
                cur_node = prev
            else:
                return head
        return head
