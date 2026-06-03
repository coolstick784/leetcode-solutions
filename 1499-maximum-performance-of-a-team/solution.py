# sort by efficiency
# get the sum of first k sorted by efficiency
# then, pop the lowest speed and add the next until there are no more to add
MOD = 10**9+7
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        for s, e in list(zip(speed, efficiency)):
            heapq.heappush(heap, (-e, -s))
        speeds = []
        cur_sum = 0
        res = -float('inf')
        while heap:

            e, s = heapq.heappop(heap)
            s = -s
            min_e = -e
            heapq.heappush(speeds, s)
            cur_sum += s
            while len(speeds) > k:
                cur_sum -= heapq.heappop(speeds)

            res = max(res, cur_sum*min_e)  
        return res % MOD
