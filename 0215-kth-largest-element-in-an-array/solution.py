class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        cur = 0
        for n in range(10**4, -10**4-1, -1):
            cur += ctr.get(n, 0)
            if cur >= k:
                return n

