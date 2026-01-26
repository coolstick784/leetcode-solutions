
class Solution:
    def maxArea(self, height: List[int]) -> int:
        tmp = height.copy()
        tmp.sort()
        max_sum = 0
        all_tried = []
        max_h = tmp[-2]
        tmp = height.copy()
        tmp.reverse()
        def getFirst(h, height):
            for idx, c in enumerate(height):
                if c >= h:
                    return idx
        def getLast(h, height):

            for idx, c in enumerate(tmp):
                if c >= h:
                    return len(height) - idx - 1

        for h in list(set(height)):
            if h > max_h:
                continue
            first = getFirst(h, height)
            last = getLast(h, height)
           
            max_sum = max((last - first) * h, max_sum)
        return max_sum 
        

        
