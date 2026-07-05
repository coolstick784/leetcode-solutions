from collections import deque
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        mx_list = deque()
        for idx, n in enumerate(nums):
            while mx_list and n > mx_list[-1][1]:
                mx_list.pop()
            mx_list.append((idx, n))
        res = -float('inf')
        for idx, n in enumerate(nums):
            while mx_list and mx_list[0][0] < (idx+k):
                mx_list.popleft()
            if mx_list:
                res = max(res, n + mx_list[0][1])
        return res
            
