class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        for idx, ch in enumerate(s):
            if ch == 'a':
                continue
            cost = ord('z') - ord(ch) + 1
            res = max(res, cost)

        return res 
