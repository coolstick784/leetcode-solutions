class Solution:
    def stringHash(self, s: str, k: int) -> str:
        letters = [chr(ord('a') + n) for n in range(26)]
        idxs = {}
        for idx, ch in enumerate(letters):
            idxs[ch] = idx
        res = []
        for idx, ch in enumerate(s):
            if idx % k == 0:
                if idx != 0:
                    res.append(letters[cur % 26])
                cur = 0

            cur += idxs[ch]
        res.append(letters[cur % 26])
        return "".join(res)
