from collections import deque
class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        swap_diffs = []
        no_swap_diff = 0
        long_swap = 0
        long_no_swap = 0
        mx_swap = min(2, len(nums))
        mx_no_swap = min(2, len(nums))
        prev = deque()
        for idx, n in enumerate(nums):

            if idx == 0:
                long_no_swap = 1
                long_swap = 1
                prev.append(1)
                continue
            if idx == 1:
                pot = [n - nums[idx-1]]
                long_no_swap = 2
                long_swap = 2
                no_swap_diff = n - nums[idx-1]
                prev.append(2)
                continue
            if n - nums[idx-1] == no_swap_diff:
                long_no_swap += 1
            else:
                no_swap_diff = n - nums[idx-1]
                long_no_swap = 2
               
            if n - nums[idx-1] in swap_diffs:
                swap_diffs = [n - nums[idx-1]]
                long_swap += 1
            else:
                swap_diffs = [n - nums[idx-1]]
                long_swap = 3
                if (n - nums[idx-2]) % 2 == 0:
                    swap_diffs.append((n-nums[idx-2]) // 2)
                    if len(prev) == 2 and idx >= 3 and (n - nums[idx-2])//2 == nums[idx-2] - nums[idx-3]:
                        long_swap = prev[0] + 2
                
            prev.append(long_no_swap)
            mx_swap = max(long_swap, mx_swap)
            mx_no_swap = max(mx_no_swap, long_no_swap)
            if len(prev) > 2:
                prev.popleft()
            

        return max(mx_swap, min(mx_no_swap+1, len(nums)))
