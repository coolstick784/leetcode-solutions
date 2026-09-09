# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None for _ in range(k)]
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        l = len(res)
        mx = math.ceil(l / k)
        mn = math.floor(l / k)
        mx_ct = 0
        mn_ct = 0
        rem = k
        while l % mx != 0 or l // mx != rem:
            mn_ct += 1
            l -= mn
            rem -= 1
        #print(mn_ct, mx_ct)
        mx_ct = l // mx
        idx = 0
        breaks = set()
        
        
        while idx < len(res) and mn_ct > 0:
            mn_ct -= 1
            
            idx += mn
            breaks.add(len(res) - idx)
        while idx < len(res) and mx_ct > 0:
            mx_ct -= 1
            
            idx += mx
            breaks.add(len(res) - idx)
        breaks.remove(0)
        breaks.add(len(res))
        #print(breaks)
        res = []
        cur = head
        idx = 1
        cur_head = head
        while cur:
            

            if idx-1 in breaks:
                
                res.append(cur_head)
                cur_head = cur
               
            if idx in breaks:
                new_next = cur.next
                cur.next = None
                cur = new_next
                idx += 1
                continue
            cur = cur.next
            idx += 1
        res.append(cur_head)

        

        while len(res) < k:
            res.append(None)
        return res


