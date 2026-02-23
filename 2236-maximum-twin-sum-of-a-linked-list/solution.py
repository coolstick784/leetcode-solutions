# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li = [head.val]
        while head.next:
            li.append(head.next.val)
            head = head.next
        max_sum = 0
        left = 0
        right = len(li) - 1
        while left < right:
            l = li[left]
            r = li[right]
            max_sum = max(max_sum, l + r)
            left += 1
            right -= 1
            
        return max_sum
        
