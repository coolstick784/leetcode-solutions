# if the leftmost bit is 0, flip it
# otherwise, move on
# at each element, we'll want to know how many times it's been flipped
# have an arr of flips, each val is 0 or 1
# if len(flips) == k, subtract flips.pop()

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = deque([])
        res = 0
        sum_flips = 0
        for idx in range(len(nums) - k+1):
            if len(flips) == k:
                sum_flips -= flips.popleft()
            if sum_flips % 2 == 0:
                cur = nums[idx]
            elif nums[idx] == 1:
                cur = 0
            else:
                cur = 1

  
            if cur == 0:
                sum_flips += 1
                flips.append(1)
                res += 1
            else:
                flips.append(0) 

        for idx in range(len(nums)-k+1, len(nums)):
            if len(flips) == k:
                sum_flips -= flips.popleft()
            if sum_flips % 2 == 0:
                cur = nums[idx]
            elif nums[idx] == 1:
                cur = 0
            else:
                cur = 1
            cur = nums[idx] - sum_flips % 2
            if cur == 0:
                return -1
            else:
                flips.append(0) 
        return res
