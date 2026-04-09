class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        prefixes = {}
        for word in words:
            cur_word = ""
            for ch in word:
                cur_word += ch
                prefixes[cur_word] = prefixes.get(cur_word, 0) + 1
        # we need to know the length, the prefix, and the count
        # sort by length (desc) -> count (desc) -> prefix (doesnt matter)
        # we only want prefixes that are populated at least k times
        # then, just loop through the prefixes 
        # if it's populated k+1 times, or the word doesn't start with it, add it
        # otherwise, move on
        p_list = []
        for p in prefixes:
            p_list.append((len(p), prefixes[p], p))
        p_list.sort()
        p_list.reverse()
        p_list = [p for p in p_list if p[1] >= k]
        res = []
        for word in words:
            cur_res = 0
            for p in p_list:
                if p[1] > k or not word.startswith(p[2]):
                    cur_res = max(cur_res, p[0])
                    break


            res.append(cur_res)
        return res
