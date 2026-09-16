class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(idx, arr):
            end = arr[idx+1:]
            og = arr[:idx+1]
            og.reverse()
            arr = og + end
            return arr
        heap = []
        for idx, n in enumerate(arr):
            heapq.heappush(heap, -n)
        ctr = 1
        res  = []
        while heap:
            mx = -heapq.heappop(heap)
            idx = arr.index(mx)
            arr = flip(idx, arr)
            arr = flip(len(arr)-ctr, arr)
            print("arr", arr)
            res.append(idx+1)
            res.append(len(arr)-ctr+1)
            ctr += 1
        return res
        
