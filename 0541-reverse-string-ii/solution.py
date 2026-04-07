class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_group(sub):
            to_reverse = sub[:k]
            rest = sub[k:]
            to_reverse = list(to_reverse)
            to_reverse.reverse()
            return "".join(to_reverse) + rest
        res = ""
        cur_idx = 0
        while cur_idx < len(s):
            res += reverse_group(s[cur_idx:cur_idx+k*2])
            cur_idx += k*2
        return res
