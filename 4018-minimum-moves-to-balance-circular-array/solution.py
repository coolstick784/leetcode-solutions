class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        if min(balance) >= 0:
            return 0
        i = 0
        for idx, n in enumerate(balance):
            if n < 0:
                i = idx
        heap = []
        k = len(balance)
        for idx, n in enumerate(balance):
            if idx == i:
                continue
            dist = min(abs(idx-i), abs(k-i+idx), abs(k-idx+i))
            heapq.heappush(heap, (dist, n))
        cur = balance[i]
        res = 0
        
        
        while cur < 0:
            d, n = heapq.heappop(heap)
            if n <= 0:
                continue
            if n > -1 * cur:
                n = -1 * cur
            cur += n
            res += d * n
            #print("cur", cur, "res", res)
        return res
