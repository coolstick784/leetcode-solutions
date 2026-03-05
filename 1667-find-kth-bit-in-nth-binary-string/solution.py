class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            out = ""
            for ch in s[::-1]:
                if ch == "1":
                    out += "0"
                else:
                    out += "1"
            return out
        @lru_cache(None)
        def getStr(n):


            if n == 1:
                return "0"
            return getStr(n-1) + "1" + invert(getStr(n-1))
        return getStr(n)[k-1]
