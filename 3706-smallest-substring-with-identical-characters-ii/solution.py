class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        ops1 = 0
        ops2 = 0

        for i, ch in enumerate(s):
            if ch != str(i % 2):        # 010101...
                ops1 += 1
            if ch != str(1 - i % 2):    # 101010...
                ops2 += 1

        if min(ops1, ops2) <= numOps:
            return 1
        
        left = 2
        right = n

        while left < right:
            med = (left + right) // 2

            cur = 0
            ctr = 1

            for i in range(1, n):
                if s[i] == s[i - 1]:
                    ctr += 1
                else:
                    cur += ctr // (med + 1)
                    ctr = 1

            cur += ctr // (med + 1)

            if cur > numOps:
                left = med + 1
            else:
                right = med

        return left
