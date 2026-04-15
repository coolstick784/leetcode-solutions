# sliding window problem
# starting at a left index, keep moving to the right until either A. the next element is not greater than the last or B. we've reached size k
# if we've reached size k, add the right index to our resolution and move the left 1 to the right
# elif the right has reached the end, return res
# elif it's <= the previous one, move the left to the new one and fill in the middle with -1s
# so basically prefill it with -1s

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1 for _ in range(len(nums)-k+1)]
        left = 0
        right = 0
        while left < len(res):
    
            diff = (right-left) + 1
            if diff == k:
                res[left] = nums[right]
                left += 1
            if right == len(nums) - 1:
                return res
            if nums[right+1] != nums[right] + 1:
                left = right+1
                right = left
            else:
                right += 1
        

        return res


# [1,2,3,4,3,2,5], k = 3
# len(res) = 5
# l 0, r 2
# res[0] = 3
# l 1, r 3 
# [3, 4]
# 
