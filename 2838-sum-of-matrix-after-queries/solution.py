import bisect
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = {}
        cols = {}
        row_idxs = []
        col_idxs = []
        ctr = 0
        for t, idx, val in queries:
            if t == 0:
                rows[idx] = (val, ctr)
                
            else:
                cols[idx] = (val, ctr)
                
            ctr += 1
        for r in rows:
            row_idxs.append(rows[r][1])
        row_idxs.sort()
        for c in cols:
            col_idxs.append(cols[c][1])
        col_idxs.sort()
        
        res = 0
        for r in rows:
            
            idx = rows[r][1]
            val = rows[r][0]
            res += val * (n - (len(col_idxs) - bisect.bisect(col_idxs, idx)))
        for c in cols:
            idx = cols[c][1]
            val = cols[c][0]
            res += val * (n - (len(row_idxs) - bisect.bisect(row_idxs, idx)))
        return res
        
        
