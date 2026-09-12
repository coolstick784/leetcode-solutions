class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        cols = {}
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                rows.setdefault(r, []).append(el)
                cols.setdefault(c, []).append(el)

        def equal(l1, l2):
           
            for idx, el in enumerate(l1):
                if el != l2[idx]:
      
                    return False
            return True
        print(rows, cols)
        res = 0
        for r in rows:
            for c in cols:
                if equal(rows[r], cols[c]):
                    res += 1
        return res
