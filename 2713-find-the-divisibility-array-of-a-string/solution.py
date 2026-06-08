# take mod, multiply by 10, add to new num
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        cur_mod = 0
        res = []
        for ch in word:
            cur_mod = ((cur_mod*10)%m + int(ch) % m) % m
            if cur_mod == 0:
                res.append(1)
            else:
                res.append(0)
        return res
