class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = set()
        blocked = set()
        seen = set()
        for idx, ch in enumerate(word):
            if ch == ch.upper():
                if ch.lower() in seen:
                    res.add(ch)

            else:
                if ch.upper() in seen:
                    blocked.add(ch.upper())
            seen.add(ch)
        res = [r for r in res if r not in blocked]
        return len(res)
