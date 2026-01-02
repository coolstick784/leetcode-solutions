# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        start = ListNode(head.val, None)
        cur_output_node = start
        cur_node = head
        while True:
            cur_node = cur_node.next
            if cur_node is None:
                return start

            if cur_node.val != cur_output_node.val:
                cur_output_node.next = ListNode(cur_node.val, None)
                cur_output_node = cur_output_node.next
        

        
