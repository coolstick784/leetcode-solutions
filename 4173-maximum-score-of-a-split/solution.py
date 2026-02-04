class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        res = -2**31
        n_sorted = sorted(nums.copy())
        cur_sum = 0
        mins = [None for _ in range(len(nums))]
        len_nums = len(nums)
        cur_min = nums[len_nums-1]
        for i, n in enumerate(nums[::-1][:-1]):
            idx = len_nums-i-2
            cur_min = min(cur_min, n)
            mins[idx] = cur_min



        for idx, n in enumerate(nums[:-1]):
            cur_sum += n
            

            res = max(res, cur_sum - mins[idx])
        return res

        
