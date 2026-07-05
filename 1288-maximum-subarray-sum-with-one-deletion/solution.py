class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) <= 0:
            return max(arr)
        best_deletion = 0
        best_no_deletion = 0
        mx = 0
        for idx, n in enumerate(arr):
            best_deletion = max(0, best_no_deletion, best_deletion + n, best_no_deletion + n)
            best_no_deletion = max(0, best_no_deletion + n)
            mx = max(mx, best_deletion, best_no_deletion)
        return mx

