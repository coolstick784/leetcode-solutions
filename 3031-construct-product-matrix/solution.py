class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        num_zeros = 0
        res = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        product = 1

        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 0:
                    num_zeros += 1
                else:
                    product = (product * el) % MOD
        
        if num_zeros != 0:
            for r, row in enumerate(grid):
                for c, el in enumerate(row):
                    if el == 0 and num_zeros == 1:
                        res[r][c] = product
                    else:
                        res[r][c] = 0
            return res

        arr = []
        for row in grid:
            for el in row:
                arr.append(el)

        prefix = 1
        for i in range(len(arr)):
            r = i // len(grid[0])
            c = i % len(grid[0])
            res[r][c] = prefix
            prefix = (prefix * arr[i]) % MOD

        suffix = 1
        for i in range(len(arr) - 1, -1, -1):
            r = i // len(grid[0])
            c = i % len(grid[0])
            res[r][c] = (res[r][c] * suffix) % MOD
            suffix = (suffix * arr[i]) % MOD

        return res
