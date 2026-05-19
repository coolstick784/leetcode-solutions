# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = [] 
        li_dict = {}

        node = head
        while node:
            li.insert(bisect.bisect(li, node.val), node.val)
            li_dict.setdefault(node.val, deque()).append(node)

            node = node.next
        li = deque(li)
        head = li_dict[li.popleft()].popleft()
        node = head
        while li:
            node.next = li_dict[li.popleft()].popleft()
            node = node.next

        node.next = None
        
        return head

