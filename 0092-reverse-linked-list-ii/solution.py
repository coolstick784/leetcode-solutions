# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# head = [1,2,3,4,5], left = 2, right = 4, dist = 3, to_next = 1
# rev(2, 3)
# q = [2, 3, 4]
# old next = 5
# new head = 4
# [4, 3, 2]
# [4, 3, 2, 5]
# return 4
# 1.next = 4
# [1, 4, 3, 2, 5]

# [5], 1, 1
# node = 5
# rev(5, 1)
# 5, old_next = None
# new head = 5
# 5, None
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. get a dist
        dist = right - left + 1
        # want a count as we go through the list
        ct = 1
        node = head
        while ct < left:
            if ct == left -1:
                to_next = node
            node = node.next
            ct += 1
        
        # once we've reached the left, create a function to reverse dist elements

        def rev(node, dist):
            cur = 0
            q = []
            while cur < dist:
                q.append(node)
                node = node.next
                cur += 1
            old_next = node

            new_head = q.pop()
            node = new_head
            while q:
                node.next = q.pop()
                node = node.next
            node.next = old_next


            return new_head
        new_head= rev(node, dist)
        if left == 1:
            head = new_head

        if left > 1:
            to_next.next = new_head

        return head
