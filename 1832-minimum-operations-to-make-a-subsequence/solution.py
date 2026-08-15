class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mp = {}
        for idx, n in enumerate(target):
            mp[n] = idx
        longest = []
        for idx, n in enumerate(arr):
            if n not in mp:
                continue
            cur = mp[n]
            if not longest or cur > longest[-1]:
                longest.append(cur)
                continue
            long_idx = bisect.bisect_left(longest, cur)
            longest[long_idx] = cur
        print(longest)
        return len(target) - len(longest)



