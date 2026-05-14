# make it T/F tiring or non tiring
# sum them up (1/-1), then for each left, we want the furthest right that's > the left

# if a number is positive, we want that index
# otherwise, we go from largest to lowest, the furthest right is max(cur, prev)

# [1, 2, 1, 0, -1, -2, -1]
# [-1, -2, -1, 0]
# [-1, 0, -1]
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        new = []
        res = 0
        for h in hours:
            if h > 8:
                new.append(1)
                res = 1
            else:
                new.append(-1)
        sums = []

        cur = 0
        idxs = {}
        for idx, n in enumerate(new):
            cur += n
            sums.append(cur)
            idxs[cur] = idx

        values = list(set(sums))
        values.sort(reverse=True)
        prev = -float('inf')
        for v in values:

            if v > 0:
                res = max(res, idxs[v] + 1)
            cur = max(idxs[v], prev)
            idxs[v] = prev
            prev = cur



                
        print("idxs", idxs)
        print("sums", sums)
        for idx, s in enumerate(sums):
            res = max(res, idxs[s] - idx)

        return res
                
