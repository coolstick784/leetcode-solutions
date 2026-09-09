class Solution:
    def countCommas(self, n: int) -> int:
        def count_36(num):
            if n < 10**3:
                return 0
            return min(n, 10**6-1) - 10**3 + 1
        def count_69(n):
            if n < 10**6:
                return 0
            return (min(n, 10**9-1) - 10**6 + 1) * 2
        def count_912(n):
            if n < 10**9:
                return 0
            return (min(n, 10**12-1) - 10**9 + 1) * 3
        def count_1215(n):
            if n < 10**12:
                return 0
            return (min(n, 10**15-1) - 10**12 + 1) * 4
        def count_15(n):
            if n < 10**15:
                return 0
            return 5

        print("36", count_69(n))
        return count_36(n) + count_69(n) + count_912(n) + count_1215(n) + count_15(n)
