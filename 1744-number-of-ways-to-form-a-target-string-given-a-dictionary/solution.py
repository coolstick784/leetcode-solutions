class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        letters = {}
        for word in words:
            for idx, ch in enumerate(word):
                letters.setdefault(ch, {}).setdefault(idx, 0)
                letters[ch][idx] += 1
        
        @lru_cache(None)
        def solve(left, right):
            if right == len(target):
                return 1
            if left == len(words[0]):
                return 0
            ch = target[right]
 
            return ((letters.get(ch, {}).get(left, 0) * solve(left+1, right+1)) + solve(left+1, right)) % (10**9+7)
        return solve(0, 0) % (10**9+7)
