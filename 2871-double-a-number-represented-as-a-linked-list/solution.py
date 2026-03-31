# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(10000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out_str = ""
        cur = head
        while cur:
            out_str += str(cur.val)
            cur = cur.next
        new = str(int(out_str) * 2)
        cur = head
        idx = 0
        while cur:
            cur.val = int(new[idx])
            idx += 1
            if idx < len(new) and not cur.next:
                cur.next = ListNode(int(new[-1]), next=None)
            cur = cur.next

        return head
