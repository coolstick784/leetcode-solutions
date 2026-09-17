class Solution:
    def findScore(self, nums: List[int]) -> int:
        explored = set()
        heap = []
        score = 0
        for idx, n in enumerate(nums):
            heapq.heappush(heap, (n, idx))
        while heap:
            n, idx = heapq.heappop(heap)
            if idx in explored:
                continue
            explored.add(idx)
            explored.add(idx-1)
            explored.add(idx+1)
            score += n

        return score
