# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Set the last's next to the head and the second to last's next to None
        # really, we can just connect the two and set the last node's Next to none
        len_l = 1
        cur = head
        if head == None:
            return head
        while cur.next is not None:
            cur = cur.next
            len_l += 1
        cur.next = head

        nth_el = len_l - (k % len_l)  - 1
        if nth_el < 0:
            return head
        #if (k % len_l) == 0:
            #return head
        
        cur = head
        print(cur.val)
        for i in range(nth_el):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
        
