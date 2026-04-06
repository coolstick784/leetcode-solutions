class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # can we just add k1 and k2, and subtract 1 from the largest difference every time?
        # [4, 4, 4, 3]
        # [4, 3, 3, 3]
        # if they are all 0, return 0
        diffs = []
        for idx in range(len(nums1)):
            diffs.append(abs(nums1[idx] - nums2[idx]))
        diffs.sort()
        diffs.reverse()
        total = k1+k2
        # what we can do is find the difference between the highest and next highest, subtract that from our total, and multiply that by all of our numbers
        # if the multiplier isn't enough to handle all, we'll divide however many we have left by the # of groups, subtract that from each, and then 
        # get the remainder, and subtract 1 from the remainder
        # e.g. if we have 4 nums, and we want to subtract 5, we subtract 5 // 4 = 1 from all then another 1 from 5 % 4 = 1
        cur_idx = 1
        cur_top = [diffs[0], 1] # [number we have, number of times we have it]
        if len(nums1) == 1:
            return abs(nums1[0] - nums2[0])**2
        cur_top2 = [] # for if there is a remainder
        while total > 0 and cur_idx < len(diffs):
            next_biggest = diffs[cur_idx]
            if next_biggest == 0:
      
                break
            cur_diff = cur_top[0] - next_biggest
            to_subtract = cur_diff * cur_top[1]
            if to_subtract <= total:
                cur_idx += 1
                cur_top = [next_biggest, cur_top[1] + 1]
                total -= to_subtract
            else:
                subtract_from_all = total // cur_top[1]
                cur_top = [cur_top[0] - subtract_from_all, cur_top[1]]
                subtract_one_from = total % cur_top[1]
                cur_top = [cur_top[0], cur_top[1] - subtract_one_from]
                cur_top2 = [cur_top[0] - 1, subtract_one_from]
                total = 0
       
        if total > 0:
            subtract_from_all = total // cur_top[1]
            cur_top = [cur_top[0] - subtract_from_all, cur_top[1]]
            subtract_one_from = total % cur_top[1]
            cur_top = [cur_top[0], cur_top[1] - subtract_one_from]
            cur_top2 = [cur_top[0] - 1, subtract_one_from]  

        if cur_top:
            cur_top[0] = max(cur_top[0], 0)
        if cur_top2:
            cur_top2[0] = max(cur_top2[0], 0)
        res = 0
        if cur_top:
            res += cur_top[0] ** 2 * cur_top[1]
        if cur_top2:
            res += cur_top2[0]**2 * cur_top2[1]
        for diff in diffs[cur_idx:]:
            res += diff**2
        return res




