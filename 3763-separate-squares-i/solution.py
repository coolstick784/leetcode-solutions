class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        left = min(y for x, y, l in squares)
        right = max(y + l for x, y, l in squares)

        total = sum(l * l for x, y, l in squares)
        target = total / 2

        def areaUnder(val):
            out = 0
            for x, y, l in squares:
                if y < val:
                    out += l * min(val - y, l)
            return out

        while right - left > 10**(-6):
            med = (left + right) / 2

            under = areaUnder(med)

            if under >= target:
                right = med
            else:
                left = med

        return right
