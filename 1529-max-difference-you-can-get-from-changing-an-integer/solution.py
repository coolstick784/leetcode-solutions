class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        res = 0
        mn = float('inf')
        mx = -float('inf')
        for x in range(10):

            for y in range(10):
                new = s.replace(str(x), str(y))
                if new[0] == '0':
                    continue
                new = int(new)
                mn = min(mn, new)
                mx = max(mx, new)
        res = max(res, mx-mn)
        return res


