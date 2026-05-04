# starting at 1, can we remove 2? if so, add (2+1) -1 to the diffs
# then, can we remove 3? if so, add (3+1) - 1 to the diffs
# and so on


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars = [1] + hBars
        vBars = [1] + vBars 
        hDiffs = [1]
        vDiffs = [1]
        hBars = set(hBars)
        vBars = set(vBars)
        starts = [num - 1 for num in hBars if num > 1]
        for start in starts:
            cur = start + 1
            while cur in hBars:
                hDiffs.append(cur - start + 1)
                cur += 1
        starts = [num - 1 for num in vBars if num > 1]
        for start in starts:
            cur = start + 1
            while cur in vBars:
                vDiffs.append(cur - start + 1)
                cur += 1
        vDiffs = set(vDiffs)
        hDiffs = list(set(hDiffs))
        hDiffs.sort()
        hDiffs.reverse()

        res = 0
        for diff in hDiffs:
            if diff in vDiffs:
                return diff*diff
        return res


