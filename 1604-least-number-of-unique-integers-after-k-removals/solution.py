class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # 5, 4, 3, 2, 1
        #  k = 8 -> 1, 7 -> 2, 5 -> 3, 2 -> 4 > 2 so we're left with 2
        # k= 10 -> 1, 9 -> 2, 7 -> 3, 4 -> 4 = 4 so we're left with 1
        ctr = Counter(arr)
        heap = list(ctr.values())
        heapq.heapify(heap)

        cur_k = k
        res = len(ctr.keys())
   
        while True:
            to_remove = heapq.heappop(heap)

            if to_remove > cur_k:
                return res
            elif to_remove == cur_k:
                return res - 1
            else:
                res -= 1
                cur_k -= to_remove
            

