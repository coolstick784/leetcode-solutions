# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the element before a, and set that next node to the head
        # Find the element after b, and set the list2's last node's next to that

        ctr = 0
        list2_end = list2
        while list2_end.next:
            list2_end = list2_end.next
        
        el_before_a = None
        el_after_b = None
        cur = list1
        while cur:
     
            if ctr == a-1:
                el_before_a = cur
            if ctr == b + 1:
                el_after_b = cur
            cur = cur.next
            ctr += 1
        el_before_a.next = list2
        print("list2 end", list2_end)
        print("el after b", el_after_b)
        list2_end.next = el_after_b
        return list1
