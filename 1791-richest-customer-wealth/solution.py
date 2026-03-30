class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = 0
        for acc in accounts:
            max_val = max(max_val, sum(acc))
        return max_val
