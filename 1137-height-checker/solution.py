class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = heights.copy()
        heights_sorted.sort()
        res = 0
        for idx in range(len(heights)):
            if heights_sorted[idx] != heights[idx]:
                res += 1
        return res
