# lru cache
# given a start, and a goal remainder n, what's the longest we can do?
# we also have to assume that there is no base goal remainder

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        idxs = {}
        for idx, n in enumerate(nums):
            n = n % k
            nums[idx] = n
            idxs.setdefault(n, []).append(idx)
        @lru_cache(1000)
        def solve(idx, rem):
            n = nums[idx]
            if rem >= n:
                goal = rem - n
            else:
                goal = (rem+k) - n
            if goal not in idxs:
                return 1
            dict_idx = bisect.bisect(idxs[goal], idx)
          
            if dict_idx >= len(idxs[goal]):
    
                return 1
            return 1 + solve(idxs[goal][dict_idx], rem)

        


        out = []
        for idx, n in enumerate(nums):
            for p in range(k):
                out.append(solve(idx, p))
        return max(out)



