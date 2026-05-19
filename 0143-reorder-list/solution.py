# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = 1
        node = head
        while node.next:
            l += 1
            node = node.next
        max_small = math.ceil(l/2)
        q_small = deque()
        q_big = deque()
        cur = 1
        node = head
        while node:
            if cur <= max_small:
                q_small.append(node)
            else:
                q_big.append(node)
            cur += 1
            node = node.next
        head = q_small.popleft()
        node = head
        while q_small or q_big:
            if q_big:
                node.next = q_big.pop()
                node = node.next
            if q_small:
                node.next = q_small.popleft()
                node = node.next
        node.next = None
        
