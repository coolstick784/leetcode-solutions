class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        vertical = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        horizontal = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def mapVert(inp):
            # return [row, column]
            return (inp % len(grid), inp // len(grid))
        def mapHor(inp):
            #return [row, column]
            return (inp // len(grid[0]), inp % len(grid[0]))
        vertical_arrs = [[] for _ in range(len(grid[0]))]
        horizontal_arr = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                horizontal_arr.append(col)
                vertical_arrs[c].append(col)
        vertical_arr = []
        for arr in vertical_arrs:
            vertical_arr.extend(arr)
        horizontal_str = "".join(horizontal_arr)
        vertical_str = "".join(vertical_arr)
        vertical_matches = set()
        horizontal_matches = set()
        left = 0
        res = 0
        def kmp_search(text, pattern):
            m = len(pattern)
            lps = [0] * m

            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            matches = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    matches.append(i - m + 1)
                    j = lps[j - 1]

            return matches
        m = len(pattern)

        horizontal_diff = [0] * (len(horizontal_str) + 1)
        for start in kmp_search(horizontal_str, pattern):
            horizontal_diff[start] += 1
            horizontal_diff[start + m] -= 1

        vertical_diff = [0] * (len(vertical_str) + 1)
        for start in kmp_search(vertical_str, pattern):
            vertical_diff[start] += 1
            vertical_diff[start + m] -= 1

        running = 0
        for i in range(len(horizontal_str)):
            running += horizontal_diff[i]
            if running > 0:
                horizontal_matches.add(mapHor(i))

        running = 0
        for i in range(len(vertical_str)):
            running += vertical_diff[i]
            if running > 0:
                vertical_matches.add(mapVert(i))
        
        res = 0
        for m in vertical_matches:
            if m in horizontal_matches:
                res += 1
        return res
