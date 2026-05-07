# get total # of substrings
# sort nums
# for eahc idx from the end, get the min idx where it'd be > target
#then, start at 1
pows = [1]
for _ in range(10**5+1):
    pows.append(2*pows[-1] % (10**9+7))
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        total = (pows[len(nums)] - 1) % (10**9+7)

        nums.sort()

        left = 0
        right = len(nums) - 1
        while left <= right:
            r = nums[right]
            l = nums[left]
            if r+l <= target:
                left += 1
            else:
           
                total -= pows[right-left]
                right -= 1

        return total % (10**9+7)
        
