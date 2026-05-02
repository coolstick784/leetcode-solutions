class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        total = {
            "a": s.count("a"),
            "b": s.count("b"),
            "c": s.count("c")
        }

        # If we don't even have enough of any char, impossible
        if total["a"] < k or total["b"] < k or total["c"] < k:
            return -1

        # Max amount allowed to remain in the middle
        limit = {
            "a": total["a"] - k,
            "b": total["b"] - k,
            "c": total["c"] - k
        }

        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            # Shrink while middle has too many of some char
            while (
                count["a"] > limit["a"] or
                count["b"] > limit["b"] or
                count["c"] > limit["c"]
            ):
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return n - best
