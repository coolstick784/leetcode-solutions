# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1 = None
        n2 = None
        k1 = k
        k2 = None
        vals = []
        l = 0
        node = head
        while node:
            l += 1
            vals.append(node.val)
            node = node.next
        
        k2 = l - k + 1
        
        ctr = 0
        node = head
        while node:
            ctr += 1
            if ctr == k:
                node.val = vals[k2-1]
            elif ctr == k2:

                node.val = vals[k-1]
            node = node.next
        


        return head
