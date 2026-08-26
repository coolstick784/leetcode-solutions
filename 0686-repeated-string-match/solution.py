class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        left = 1
        right = len(b) // len(a) + 5
        starts = [idx for idx, n in enumerate(a)]

        def possible(n):
            s = ""
            for _ in range(n):
                s += a
            for start in starts:
                if s[start:start+len(b)] == b:
                    return True
            return False
        if not possible(right):
            return -1
        while left < right:
            med = (left + right) // 2
            if possible(med):
                right = med
            else:
                left = med + 1
        return left
