class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        heap = []

        for n in ctr:
            heapq.heappush(heap, -1*ctr[n])
        res = 0
        cur_len = len(arr)
        goal_len = cur_len / 2
        
        while cur_len > goal_len:

            highest = -1 * heapq.heappop(heap)
            cur_len -= highest
            res += 1
        return res
