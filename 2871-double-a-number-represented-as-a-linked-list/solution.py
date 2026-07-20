# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(start):
            prev = None
            cur = start
            while cur:
                new = cur.next
                cur.next = prev
                prev = cur
                cur = new
            return prev



        revd = reverse(head)
        cur = revd
        carry = 0
        while cur:
            val = cur.val
            val += val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            cur.val = val
            if not cur.next and carry:
                cur.next = ListNode(0, None)
                
            cur = cur.next
        
        



        return reverse(revd)
