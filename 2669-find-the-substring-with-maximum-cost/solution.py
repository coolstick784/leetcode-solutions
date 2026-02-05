class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs = {}
        res = 0
        for ch in range(26):
            costs[chr(ch + ord('a'))] = 1 + ch

        for idx, ch in enumerate(chars):
            costs[ch] = vals[idx]
        condensed = []

        cur = 0
        for idx, ch in enumerate(s):
            cost = costs[ch]

            cur = max(cur + cost, 0)
            res = max(res, cur)

        
        return res
        
