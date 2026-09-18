class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        cur_idx = k
        while cur_idx < len(word) and not word.startswith(word[cur_idx:]):
            cur_idx += k
            res += 1
        return res
