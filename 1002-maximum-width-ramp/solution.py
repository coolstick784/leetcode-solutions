class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # What the question is asking is: For a number in the array, i, what is the rightmost index in the array that 
        #is equal to or higher than the number?
        # First, define a dictionary where we have the last index of each individual number
        # Then, cascade down -- starting from the highest, if the index of the number lower than it is less than it, replace it
        # For example, let's say 50 has a highest index of 30
        # then, 45 has a highest index of 20
        # We'd move from 56 -> 45, so 45 would then have a highest index of 30

        last_all = {}
        all_nums = set()
        for idx, n in enumerate(nums):
            last_all[n] = idx
            all_nums.add(n)
        all_nums = list(set(all_nums))
        all_nums.sort()
        all_nums.reverse()
        for idx, num in enumerate(all_nums[:-1]):
            cur_idx = last_all[num]
            next_idx = last_all[all_nums[idx+1]]
            if cur_idx >= next_idx:
                last_all[all_nums[idx+1]] = cur_idx
        
        res = 0
        for idx, n in enumerate(nums):
            res = max(res, last_all[n] - idx)
        return res

