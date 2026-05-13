# max is going to be limit * 2
# min is going to be 2
# for each pair, you either have to change 0, 1, or 2 numbers for each target
# if the max value of the pair + limit < target, we have to change 2
# if the min value of the pair is >=, we also have to change 2
# otherwise, we have to change 1
# if it's equal, we have to change 0
# so we can have a max values dict, min values dict, and equal values dict
# the max values dict should contain the number of each max value (e.g. if there are 2 pairs with a max of 3, 3: 2)
# similar with the min values dict
# the max values dict should be additive, so everything at 3 should be everything at 1 + everythign at 2 + everything at 3
# the min values dict should be additive but on the way down
# the equal values dict should have the number at each sum, e.g. if two pairs sum to 3 we have 3:2
# then, our answer for each possibility t is len(nums) // 2 + max_values.get(t-limit-1, 0) + min_values.get(t+1, 0) - equal_values.get(t, 0)


# max_values = {3:1, 4: 1}
# min_values = {1:1, 2:1}
# equal values = {4:1, 6:1}
# max_values = {1:0, 2:0, 3:1, 4:2}
# min_values = {4:0, 3:0, 2:1, 1:2}

# 2: 3, 3: 2, 4: 1, 5: 

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        max_poss = limit*2
        min_poss = 2
        max_values = {}
        min_values = {}
        equal_values = {}
        res = float('inf')

        left = 0
        right = len(nums) - 1
        while left < right:
            l = nums[left]
            r = nums[right]
            mx = max(l, r)
            mn = min(l, r)
            max_values[mx] = max_values.get(mx, 0) + 1 
            min_values[mn] = min_values.get(mn, 0) + 1 
            sm = l + r
            equal_values[sm] = equal_values.get(sm, 0) + 1
            left += 1
            right -= 1
        base = len(nums) // 2
        max_val = max(nums)
        min_val = min(nums)
        for n in range(1, max_poss+1):
            max_values[n] = max_values.get(n-1, 0) + max_values.get(n, 0)
        for n in range(max_poss, 0, -1):
            min_values[n] = min_values.get(n+1, 0) + min_values.get(n, 0)
        for t in range(min_poss, max_poss+1):
            res = min(res, base+max_values.get(t-limit-1, 0) + min_values.get(t, 0) -equal_values.get(t, 0))
        return res
