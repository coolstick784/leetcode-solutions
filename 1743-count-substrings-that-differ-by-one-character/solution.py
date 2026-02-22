class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        min_len = min(len(s), len(t))
        len_s = len(s)
        len_t = len(t)
        res = 0
        letters = [chr(ord('a') + i) for i in range(26)]
        for n_chars in range(0, min_len):
            s_substrs = []
            for start_idx in range(0, len_s - n_chars):
                s_substrs.append(s[start_idx:start_idx+n_chars+1])
            t_substrs = []
            for start_idx in range(0, len_t - n_chars):
                t_substrs.append(t[start_idx:start_idx+n_chars+1])
            for s_substr in s_substrs:
                for t_substr in t_substrs:
                    for replace_idx in range(len(s_substr)):
                        if s_substr != t_substr and s_substr[:replace_idx] + s_substr[replace_idx+1:] == t_substr[:replace_idx] + t_substr[replace_idx+1:]:
                            res += 1
        return res
            
        
