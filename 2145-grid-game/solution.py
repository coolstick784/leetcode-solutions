class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sums = {}
        for r, row in enumerate(grid):
            sums.setdefault(r, [0])
            for c, el in enumerate(row):
                sums[r].append(el + sums[r][-1])
        def solve(start, end):
            if start == 0:
                return sums[0][-1] - sums[0][end+1]
            if start == 1:
                return sums[1][end]

        def getBest(turn):
            return max(solve(0, turn), solve(1, turn))
        res = float('inf')
        print(sums)
        for t in range(len(grid[0])):
            res = min(res, getBest(t))
            print("t", t, "res", res)
        return res
