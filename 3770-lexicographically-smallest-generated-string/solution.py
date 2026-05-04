# initialize the output arr to be none for each
# then, for each true, set the substring accordingly
# if the index is not none, return ""
# for everything that's left, if 1. the first char of str2 is A and b. everything after it matches, the None becomes b. otherwise, it's a

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        out = [None for _ in range(len(str1) + len(str2)-1)]
        if "a" + str2[:-1] == str2:
            can_put_a = False
        else:
            can_put_a = True
        for idx, ch in enumerate(str1):
            if ch == 'F':
                continue

            for idx2, new_ch in enumerate(str2):
                out_idx = idx + idx2

                if out[out_idx] is not None and out[out_idx] != new_ch:
                    return ""
                out[out_idx] = new_ch
        l_str2 = list(str2)
        for idx, ch in enumerate(out):
            if idx > len(str1) - 1 or str1[idx] != 'F':
                continue
            if out[idx:idx+len(str2)] == l_str2:
                return ""
        none_idxs = []
        for idx, ch in enumerate(out):
            if ch is None:
                out[idx] = 'a'
                none_idxs.append(idx)

        for idx, ch in enumerate(out):
            if idx > len(str1) - 1 or str1[idx] != 'F':
                continue
            if out[idx:idx+len(str2)] == l_str2:
                cur = 'z'
                to_replace = bisect.bisect(none_idxs, idx+len(str2)-1) 
                while cur == 'z':
                    to_replace -= 1
                    if to_replace == -1:
                        return ""
                    cur = out[none_idxs[to_replace]]

                    
                out[none_idxs[to_replace]] = chr(ord(cur) + 1)
        
        print("out", out)
        return "".join(out)

