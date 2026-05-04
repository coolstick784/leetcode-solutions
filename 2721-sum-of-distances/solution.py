# [1, 2, 3, 4]
# 1 -> 10 - (1*4) = 6 + 0 = 6
# 2 -> 9 - (2*3) + 2*1 - (1) = 4
# 3 -> 7 - (3*2) + 3*2 - (3) = 4
# 4 -> 4 - (4*1) +  4* 3 - (6) = 6
# for each list of indices, we want to know the sum after (including), the sum before (not including), the number we're on, and the number after

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = [None for _ in nums]
        num_dict = {}
        for idx, n in enumerate(nums):
            num_dict.setdefault(n, []).append(idx)
        for n in num_dict:
            sum_after = sum(num_dict[n])
            sum_before = 0
            num_before = 0
            num_after = len(num_dict[n])
            for idx in num_dict[n]:
                arr[idx] = sum_after - num_after * idx + num_before * idx - sum_before
                sum_before += idx
                num_before += 1
                num_after -= 1
                sum_after -= idx
        return arr 
