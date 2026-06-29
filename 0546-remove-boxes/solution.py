class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        new = []

        for color in boxes:
            if new and new[-1][0] == color:
                oldColor, oldCt = new.pop()
                new.append((oldColor, oldCt + 1))
            else:
                new.append((color, 1))

        @lru_cache(None)
        def solve(start, end, carryCt):
            if start > end:
                return 0

            curColor, curCt = new[start]
            totalCt = curCt + carryCt

            res = totalCt * totalCt + solve(start + 1, end, 0)

            for mid in range(start + 1, end + 1):
                if new[mid][0] == curColor:
                    res = max(
                        res,
                        solve(start + 1, mid - 1, 0) +
                        solve(mid, end, totalCt)
                    )

            return res

        return solve(0, len(new) - 1, 0)
