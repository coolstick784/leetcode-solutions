from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1] * n for _ in range(m)]          # -1 means "unvisited"
        q = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r, c))

        # normal BFS; use res as visited + distance
        while q:
            r, c = q.popleft()
            d = res[r][c] + 1
            if r > 0 and res[r-1][c] == -1:
                res[r-1][c] = d; q.append((r-1, c))
            if r+1 < m and res[r+1][c] == -1:
                res[r+1][c] = d; q.append((r+1, c))
            if c > 0 and res[r][c-1] == -1:
                res[r][c-1] = d; q.append((r, c-1))
            if c+1 < n and res[r][c+1] == -1:
                res[r][c+1] = d; q.append((r, c+1))

        return res
