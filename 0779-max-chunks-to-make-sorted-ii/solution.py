# starting from the left, we need the first n characters to be in the first n indicies

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = arr.copy()
        s.sort()
        need = {}
        have = {}
        res = 0
        for idx, n in enumerate(arr):
            goal = s[idx]
            need[goal] = need.get(goal, 0) + 1

            have[n] = have.get(n, 0) + 1
            for num in have:
                ct = have[num]
                removed = min(ct, need.get(num, 0))
                have[num] -= removed
                if num in need:
                    need[num] -= removed
            
            if sum(need.values()) == 0:
                res += 1




        return res
        
