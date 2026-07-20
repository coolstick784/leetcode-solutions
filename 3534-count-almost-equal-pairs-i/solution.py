from collections import Counter
# 5 + 4 + 3 + 2 + 1
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        
        
        nums = [str(n) for n in nums]
        for idx, n in enumerate(nums):
            while len(n) < 8:
                n = "0" + n
            nums[idx] = n
        ctr = Counter(nums)
        res = 0
        for idx, n in enumerate(nums):
            explored = set()
            
            ctr[n] -= 1
            n = list(n)
            for ch_idx in range(8):
                for second_idx in range(ch_idx+1, 8):
                    n[ch_idx], n[second_idx] = n[second_idx], n[ch_idx]
                    s = "".join(n)
                    if s not in explored:
                        res += ctr.get("".join(s), 0)
                        explored.add(s)
                    n[ch_idx], n[second_idx] = n[second_idx], n[ch_idx]
        return res


