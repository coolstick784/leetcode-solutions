# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        cur_node = head.next 
        prev = head
        while cur_node:
            new = cur_node.next
            if cur_node.val in nums:
                prev.next = new
                cur_node = new
            else:
                prev = cur_node
                cur_node = new

        return head

