class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res = 0
        # Want to know if everything before the index is below the value, and if everything after is higher
        # If not, we want to know if the last value is lower and the next value is higher

        # We want to know the maximum value before the index and the minimum value after
        # If it's > the max and < the min, sum = 2
        # Otherwise, if it's > prev and < next, add 1

        max_before = [-2**31]
        min_after = [2**31]
       
        for n in nums:
            max_before.append(max(max_before[-1], n))
        for n in nums[::-1]:
            min_after.append(min(min_after[-1], n))
        min_after= min_after[::-1][1:]

        print("max before", max_before)
        print("min after", min_after)

        for idx, n in enumerate(nums):
            if idx == 0 or idx == len(nums) -1:
                continue
            if n > max_before[idx] and n < min_after[idx]:
                res += 2
            elif n > nums[idx-1] and n < nums[idx+1]:
                res += 1
        return res

        
