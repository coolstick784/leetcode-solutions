import heapq
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        heap = []
        stack = []
        greater = {}
        res = []
        for idx, n in enumerate(nums):
            while heap and heap[0][0] < n:
                p_num, p_idx = heapq.heappop(heap)
                greater[p_idx] = idx
            while stack and stack[-1][0] < n:
                heapq.heappush(heap, stack.pop())
            stack.append((n, idx))
        for idx, n in enumerate(nums):
            p = greater.get(idx)
            if p:
                res.append(nums[p])
            else:
                res.append(-1)
        return res
