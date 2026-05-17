# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        ns = set(nums)
        
        def solve(node):
            while node and node.val in ns:
                node = node.next
            if node:
                node.next = solve(node.next)
            return node
        return solve(head)
