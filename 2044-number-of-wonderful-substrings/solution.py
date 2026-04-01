class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        seen = {0: 1}   # how many times we've seen each state
        state = 0       # which letters currently have odd counts
        ans = 0

        for ch in word:
            bit = ord(ch) - ord('a')
            state ^= (1 << bit)   # flip this letter between even/odd

            # case 1: all letters in substring have even counts
            ans += seen.get(state, 0)

            # case 2: exactly one letter in substring has odd count
            for i in range(10):
                almost_same = state ^ (1 << i)
                ans += seen.get(almost_same, 0)

            seen[state] = seen.get(state, 0) + 1

        return ans
