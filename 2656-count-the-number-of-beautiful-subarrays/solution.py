# if two elements are the same, they cancel each other out
# if an arr is beautiful, the number of beautiful arrays starting at the left = 1 + number of arrs starting at right + 1



class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor = [0]
        for n in nums:

            xor.append(xor[-1]^n)
        ctr = Counter(xor)
        res = 0
        for n in ctr:
            res += (ctr[n]) * (ctr[n] - 1) // 2
        return res
