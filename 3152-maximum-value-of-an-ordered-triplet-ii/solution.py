# for a given j, we want to know the highest number before it as well as the highest number after it
# the one before it is i, and the one after it is k
# we can loop through twice, once to find k and then once to loop through j/get the runing max for i

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_after = [-1]
        cur_max = -1
        for idx, n in enumerate(nums[::-1][:-1]):
            cur_max = max(cur_max, n)
            max_after.append(cur_max)
        max_after.reverse()
        cur_max = -1
        res = 0
        for idx, n in enumerate(nums[:-1]):
            res = max(res, (cur_max-n) * max_after[idx])

            cur_max = max(cur_max, n)
        return res
