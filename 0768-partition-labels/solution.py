# we want the last index of each letter
# so e.g. we start at a, we want the last index of a
# then, we check each letter between the first and last index (inclusive), and our last index is then the max(last_index, last index of cur letter)
# then, once the cur index is the last index, appned last - first + 1index to the result, and move first to last_index + 1
# while first index < len(s)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_idx = 0
        last_idx = -1
        last_idxs = {}
        cur_idx = 0
        res = []
        for idx, ch in enumerate(s):
            last_idxs[ch] = idx
        while first_idx < len(s):
            cur_ch = s[cur_idx]
            last_idx = max(last_idx, last_idxs[cur_ch])
            if cur_idx == last_idx:
                res.append(last_idx-first_idx+1)
                first_idx = last_idx + 1
                cur_idx = first_idx
            else:
                cur_idx += 1
        return res
            
