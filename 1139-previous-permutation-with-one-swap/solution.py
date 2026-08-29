import heapq
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        heap = []

        idx = len(arr) - 1
        mn = float('inf')
        while idx >= 0:
            n = arr[idx]
            if n > mn:
                while n <= -heap[0][0]:
                    heapq.heappop(heap)
                s_idx = heap[0][1]
                arr[idx], arr[s_idx] = arr[s_idx], arr[idx]
                return arr
            

            mn = n
            heapq.heappush(heap, (-n, idx))

            idx -= 1
  
        return arr
