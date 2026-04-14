class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        start_idx = 0
        while start_idx < len(s):
            end_idx = start_idx
            cur_s = s[start_idx]
            while cur_s in seen and end_idx < (len(s)-1):
                end_idx += 1
                cur_s += s[end_idx]
            if cur_s not in seen:
                seen.add(cur_s)
                res.append(cur_s)
            start_idx = end_idx + 1
        return res
