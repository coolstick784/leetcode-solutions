# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur_node = head
        def checkN(c_node):
            ctr = 0

            while ctr < n:
                c_node = c_node.next
                ctr += 1
            if c_node == None:
                return True
            return False
        while True:
            if checkN(cur_node):

                if head == cur_node:
                    head = cur_node.next
                else:

                    past_node.next = cur_node.next
                return head
            else:

                past_node = cur_node
                cur_node = cur_node.next

        
        return head
        
