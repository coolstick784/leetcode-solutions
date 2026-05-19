# have a start index
# then, for each start index, get the index of each word
# the extra cost will be everything before that index + the extra cost of everything after
# s = "sayhelloworld", dictionary = ["hello","world"]
# 3 + 0 + 0
# 8 + 0
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        @lru_cache(None)
        def solve(cur):
            if cur == "":
                return 0
            res = len(cur)
            for word in dictionary:
                if word in cur:
                    idx = cur.index(word)
                    res = min(res, idx + solve(cur[idx+len(word):]))
            return res

        return solve(s)
