import copy
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = {} # start, end, h
        all_mx = 0
        res = []
        for left, length in positions:
            mx = 0
            right = left + length
            to_change = []
            og = copy.deepcopy(heights)
            for start in og:
                for end in og[start]:
                    h = heights[start][end]
                    if start <= left and end <= left:
                        continue
                    if start >= right and end >= right:
                        continue
                    
                    if start >= left and end <= right:
                        del heights[start][end]
                        mx = max(mx, h)
                    elif start < left and end > right:
                        heights[start][left] = h
                        heights.setdefault(right, {})[end] = h
                        del heights[start][end]
                        mx = max(mx, h)
                 
                    elif start < left and end <= right:
                        del heights[start][end]
                        heights[start][left] = h
                        mx = max(mx, h)
                    elif start < right and end > right:
                        del heights[start][end]
                        heights.setdefault(right, {})[end] = h
                        mx = max(mx, h)
            heights.setdefault(left, {})[right] = mx + length
            all_mx = max(all_mx, heights[left][right])
            res.append(all_mx)
        return res
                
                

