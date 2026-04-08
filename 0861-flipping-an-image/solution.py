class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = image.copy()
        for r, row in enumerate(image):
            left = 0 
            right = len(row) - 1
            while left <= right:
                res[r][left], res[r][right] = res[r][right], res[r][left]
                res[r][left] = 1 - res[r][left]
                if left < right:
                    res[r][right] = 1 - res[r][right]

                left += 1
                right -= 1
        return res
