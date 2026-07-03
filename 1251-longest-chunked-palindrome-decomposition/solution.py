class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        left = 0
        right = len(text) - 1

        @lru_cache(None)
        def sub(left, right):
            return text[left:right+1]
        cleared_left = 0
        cleared_right = len(text) - 1
        curL = 0
     
        while cleared_left < cleared_right:
            l = sub(cleared_left, cleared_left+curL)
            r = sub(cleared_right-curL, cleared_right)
            if cleared_left + curL >= cleared_right:
                res += 1
                cleared_left = cleared_left+curL+1
            elif l == r:
                
                res += 2
                cleared_left = cleared_left+curL + 1
                cleared_right = cleared_right-curL-1
                print("left", cleared_left, "right", cleared_right)
                curL = 0
            else:
                curL += 1

        if cleared_left == cleared_right:
            res += 1
        return res 
