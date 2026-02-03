from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        ctr = Counter(nums)
        poss = [n for n in range(nums[0], nums[-1] + 1)]
        left = 0
        left_val = nums[0]
        right = 0
        right_val = nums[0]



        res = {}
        next_val = nums[1]

        for p in poss:
            left_val = nums[left]

            while left < len(nums) and left_val < p - k:
                left += 1
                left_val = nums[left]
            if right < len(nums) - 1:
                next_val = nums[right+1]
      
 
            while right < len(nums) - 1 and next_val <= p + k:
                right_val = next_val

                next_val = nums[right+1]

                right += 1
            if nums[right] > p+k:
                right -= 1
            


            res[p] = right - left + 1



        for n in poss:
            if res[n] > numOperations:
                diff = res[n] - numOperations
                res[n] = numOperations + min(diff, ctr.get(n, 0))


        return max(res.values())

        


        

        
