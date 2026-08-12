# start with the minimum from each list
# continue to pop the minimum from all and replace it with the next
# once there are no elements in the minimum list, return res

from collections import deque
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums = [deque(l) for l in nums]
        cur = []
        mx = -float('inf')
        for idx, l in enumerate(nums):
            val = l.popleft()
            mx = max(mx, val)
            heapq.heappush(cur, (val, idx))
        res = float('inf')
        out = []
        while True:
            mn, l_idx = heapq.heappop(cur)
            if mx - mn < res:
                res = mx - mn
                out = [mn, mx]
            if nums[l_idx]:
                val = nums[l_idx].popleft()
                mx = max(mx, val)
                heapq.heappush(cur, (val, l_idx))
            else:
                return out

