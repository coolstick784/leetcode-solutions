# we can do a min of "min even", "min odd"
# for each index, we can have the current value, and if it's even or odd
# if it's even, and the index is even, we have to decrement the next char until it's less than the current, decrementing the current chracter will not help
# if it's even, and the index is odd, we have to decrement the current char until it's less than the next
# if it's odd, and the index is odd, we have to decrement the next char until it's less than the current
# if it's odd, and the index is even, we have to decrement the cur char until it's less than the next
# if it's the len -1, return 0
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        

        @lru_cache(None)
        def solve(idx, val, is_even):
            if idx == len(nums) - 1:
                return 0
            if is_even:
                if idx % 2 == 0:
                    if nums[idx+1] >= val:
                        diff = nums[idx+1] - (val-1)
                        return diff + solve(idx+1, val-1, is_even)
                    else:
                        return solve(idx+1, nums[idx+1], is_even)
                else:
                    if val >= nums[idx+1]:
                        diff = val - (nums[idx+1]-1)
                        return diff + solve(idx+1, nums[idx+1], is_even)
                    else:
                        return solve(idx+1, nums[idx+1], is_even)
            else:
                if idx % 2 == 0:
                    if val >= nums[idx+1]:
                        diff = val - (nums[idx+1]-1)
                        return diff + solve(idx+1, nums[idx+1], is_even)
                    else:
                        return solve(idx+1, nums[idx+1], is_even) 
                else:
                    if nums[idx+1] >= val:
                        diff = nums[idx+1] - (val-1)
                        return diff + solve(idx+1, val-1, is_even)
                    else:
                        return solve(idx+1, nums[idx+1], is_even)
        return min(solve(0, nums[0], True), solve(0, nums[0], False))
