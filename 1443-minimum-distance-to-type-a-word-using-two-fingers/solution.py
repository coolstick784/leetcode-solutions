class Solution:
    def minimumDistance(self, word: str) -> int:

        @lru_cache(None)
        def getCoords(l):
            x = (ord(l) - ord('A')) % 6
            y = (ord(l) - ord('A')) // 6

            return (x, y)

        @lru_cache(None)
        def getDist(l1, l2):
            if l1 is None:
                return 0
            x1, y1 = getCoords(l1)
            x2, y2 = getCoords(l2)
            return abs(x1-x2) + abs(y1-y2)
            
        @lru_cache(None)
        def solve(f1spot, f2spot, idx):
            if idx == len(word):
                return 0
            letter = word[idx]
            return min(getDist(f1spot, letter) + solve(letter, f2spot, idx+1), getDist(f2spot, letter) + solve(f1spot, letter, idx+1))

        return solve(None, None, 0)
