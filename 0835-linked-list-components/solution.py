# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        node = head
        res = 0
        prev = False
        while node:
            
            if node.val in nums and not prev:
                res += 1
            if node.val in nums:
                prev = True
            else:
                prev = False
            node = node.next
        return res
