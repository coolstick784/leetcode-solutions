import bisect
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_starts = []
        b_starts = []
        a = list(a)
        b = list(b)
        s = list(s)
        la = len(a)
        lb = len(b)
        for idx, ch in enumerate(s):
            if idx <= (len(s) - len(a)) and s[idx:idx+la] == a:
                a_starts.append(idx)
            if idx <= (len(s) - len(b)) and s[idx:idx+lb] == b:
                b_starts.append(idx)

        res = []
        for a in a_starts:
            mn = a - k
            mx = a + k
            b_idx = bisect.bisect(b_starts, mx) - 1
  
            if b_idx < len(b_starts) and b_idx >= 0 and b_starts[b_idx] >= mn and b_starts[b_idx] <= mx:
                res.append(a)

        return res
