# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None

        
        lt_q = deque()
        ge_q = deque()
        node = head
        while node:
            if node.val >= x:
                ge_q.append(node)
            else:
                lt_q.append(node)
            node = node.next
        q = lt_q + ge_q
        head = q.popleft()
        node = head

        while q:
            
            node.next = q.popleft()
            node = node.next
        node.next = None




        return head
