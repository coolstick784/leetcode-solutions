from collections import deque
import heapq
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        nums = [ord(ch) - ord('a') for ch in s]
        long = {}
        res = 0
        for idx in range(len(nums)-1, -1, -1):
            n = nums[idx]
            for p in range(k+1):
                long[n] = max(long.get(n, 0), long.get(n-p, 0) + 1, long.get(n+p, 0) + 1)

            res = max(res, long.get(n, 0))

        return res
