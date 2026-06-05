pows = [2**x for x in range(32)]
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        look = {}
        best = {}
        mx = 0
        res = [[-1, -1] for _ in queries]
        for idx, [start, end] in enumerate(queries):
            xor = start ^ end
            look.setdefault(xor, []).append(idx)
            mx = max(mx, xor)

        print("look", look)
        for right in range(len(s)-1, -1, -1):
            left = right
            cur = 0
            if s[left] == "0" and 0 in look:
                best[0] = [1, left, left]

            while left >= 0 and cur <= mx and right - left < 32:
                if s[left] == "0":
                    left -= 1
                    continue
                cur = cur | pows[right-left]
                
                if cur in look:
                    if best.get(cur, [float('inf'), 0, 0])[0] >= right-left+1:
                        best[cur] = [right-left+1, left, right]
                left -= 1
        for cur in best:
            score, left, right = best[cur]
            for idx in look[cur]:
                res[idx] = [left, right]

        return res
