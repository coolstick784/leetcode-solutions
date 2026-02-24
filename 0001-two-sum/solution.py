class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ctr = {}
        for idx, n in enumerate(nums):
            ctr.setdefault(n, []).append((n, idx))

        for idx, n in enumerate(nums):
            if target - n in ctr:
                if target-n != n:

                    return [idx, ctr[target-n][0][1]]
                elif len(ctr[target-n]) > 1:
                    return [ctr[n][0][1],ctr[n][1][1]] 
