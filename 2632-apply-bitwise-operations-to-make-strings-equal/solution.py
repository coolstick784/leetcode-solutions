class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # if s[i] = 0 and s[j] = 1, s[j] -> 1 and s[i] -> 1
        # if s[i] = 1 and s[j] = 0, s[j] -> 1 and s[i] -> 1
        # if s[i] = 0 and s[j] = 0, both stay 0
        # if both are 1, s[i] -> 1 and s[j] -> 0
        # if there is at least one 1, it should be doable?

        if "1" in s and "1" in target:
            return True
        if "1" not in s and "1" not in target:
            return True
        return False
