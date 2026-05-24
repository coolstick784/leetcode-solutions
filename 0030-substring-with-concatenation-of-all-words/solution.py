class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wctr = Counter(words)
        l = len(words[0])
        res = []
        explored = set()
        all_words = []
        for idx in range(len(s)-l+1):
            all_words.append(s[idx:idx+l])
        def solve(start, cur_words):
            if len(cur_words.keys()) == 0:
                return True
            if start + l -1 >= len(s):
                return False
            
            word = all_words[start]
            new = cur_words.copy()
            if new.get(word, 0) > 0:
                new[word] -= 1
                if new[word] == 0:
                    del new[word]
                if solve(start+l, new):
                    return True
            return False
        for idx in range(len(s) - l * len(words)+1):
            if idx in explored:
                continue

            if solve(idx, wctr):
                res.append(idx)
                end = idx + l * len(words)
                cur = idx
                while end + l -1 < len(s) and s[cur:cur+l] == s[end:end+l]:
                    res.append(cur+l)
                    explored.add(cur+l)
                    cur = cur + l
                    end = cur + l * len(words)
        return res


                



        
