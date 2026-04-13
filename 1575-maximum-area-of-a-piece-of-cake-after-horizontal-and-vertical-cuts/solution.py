class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_x = 0
        horizontalCuts.sort()
        for idx, cut in enumerate(horizontalCuts):
            if idx == 0:
                max_x = max(max_x, cut)
            else:
                max_x = max(max_x, cut - horizontalCuts[idx-1])
            if idx == len(horizontalCuts) - 1:
                max_x = max(max_x, h - cut)
        max_y = 0
        verticalCuts.sort()
        for idx, cut in enumerate(verticalCuts):
            if idx == 0:
                max_y = max(max_y, cut)
            else:
                max_y = max(max_y, cut - verticalCuts[idx-1])
            if idx == len(verticalCuts) - 1:
                max_y = max(max_y, w - cut)
        return max_x * max_y % (10**9+7)
        
