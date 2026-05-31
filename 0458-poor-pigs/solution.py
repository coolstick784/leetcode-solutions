class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        spaces = tests + 1
        cur = 1
        res = 0

        while cur < buckets:
            res += 1
            cur *= spaces
        return res
