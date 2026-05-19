# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# head = [1,2,3,3,4,4,5]
# [1, 2, 5]
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(node, prev):
            if not node:
                return None
            if (node.next and node.val == node.next.val) or node.val == prev:
                return solve(node.next, node.val)
            elif node.next:
                node.next = solve(node.next, node.val)
            return node
        return solve(head, -200)
