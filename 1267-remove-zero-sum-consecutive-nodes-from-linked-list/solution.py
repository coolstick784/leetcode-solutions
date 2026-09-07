# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums = [0]
        idxs = {}
        cur = head
        ctr = 1
        idxs[0] = [0]
        while cur:
            sums.append(cur.val + sums[-1])
            idxs.setdefault(sums[-1], []).append(ctr)
            cur = cur.next
            ctr += 1
        starts = []
        for v in idxs:
            if len(idxs[v]) < 2:
                continue
            for i1, idx1 in enumerate(idxs[v]):
                for i2, idx2 in enumerate(idxs[v][i1+1:]):
                    starts.append((idx1+1, idx2))
        
        starts.sort()
        print(starts)
        
        
        ctr = 1
        cur = head
        
        cur_start = -1
        cur_end = -1

        for s_idx, (start, end) in enumerate(starts):
            if start <= cur_end:
                continue
            cur_end = end
            cur_start = start
            while ctr < (start-1):
                ctr += 1
                cur = cur.next
            while ctr + 1 >= start and ctr + 1 <= end:
                print("deleting", ctr+1)
                cur.next = cur.next.next
                ctr += 1
        if starts and starts[0][0] == 1:
 
            return head.next
        return head
