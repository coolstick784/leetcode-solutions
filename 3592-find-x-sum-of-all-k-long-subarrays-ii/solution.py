from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        ctr = {}
        heap = []
        rev_heap = [] # highest to lowest
        in_heap = set()
        s = 0
        for idx, n in enumerate(nums):
            
            if idx >= k:
                p = nums[idx-k]
                ctr[p] -= 1
                if len(in_heap) == x and p in in_heap:
                
                    while rev_heap and (-rev_heap[0][1] in in_heap or -rev_heap[0][0] != ctr[-rev_heap[0][1]]):
                        heapq.heappop(rev_heap)
                    
                    if rev_heap and (-rev_heap[0][0] > ctr[p] or (-rev_heap[0][0] == ctr[p] and -rev_heap[0][1] > p)):
                        rep_ct, rep_n = heapq.heappop(rev_heap)
                        rep_ct = -rep_ct
                        rep_n = -rep_n
                        
                        in_heap.remove(p)
                        in_heap.add(rep_n)
                        heapq.heappush(rev_heap, (-ctr[p], -p))
                        heapq.heappush(heap, (rep_ct, rep_n))
                        s -= (ctr[p] + 1) * p
                        s += rep_ct * rep_n
                    else:
                        heapq.heappush(heap, (ctr[p], p))
                        s -= p
                elif p in in_heap:
                    heapq.heappush(heap, (ctr[p], p))
                    s -= p 
         
            ctr[n] = ctr.get(n, 0) + 1 
            while heap and (heap[0][1] not in in_heap or heap[0][0] != ctr[heap[0][1]]):
                heapq.heappop(heap)
            
            if len(in_heap) < x:
               
                heapq.heappush(heap, (ctr[n], n))
                in_heap.add(n)
                s += n
            else:
                if n in in_heap:
                    
                    heapq.heappush(heap, (ctr[n], n))
                    s += n
                else:

                    if ctr[n] > heap[0][0] or (ctr[n] == heap[0][0] and n > heap[0][1]):
                        s += n * ctr[n]
                        rem_ct, rem_n = heapq.heappop(heap)
                        s -= rem_n * rem_ct
                
                        heapq.heappush(rev_heap, (-rem_ct, -rem_n))
             
                        heapq.heappush(heap, (ctr[n], n))
                        in_heap.add(n)
                        in_heap.remove(rem_n)
                    else:
                        heapq.heappush(rev_heap, (-ctr[n], -n))
            
            if idx < k-1:
                continue
        
            res.append(s)
        return res
