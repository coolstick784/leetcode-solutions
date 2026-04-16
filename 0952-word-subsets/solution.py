# we can get a counter of each word in words1, and a total of words in words2

# we have a dict mapping each letter
# thenm for each word in words1, we count it, and we check if each count for each letter is >= the count in words2

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        count_dict = {}
        for word in words2:
            ctr = Counter(word)
            for ch in ctr:
                count_dict[ch] = max(count_dict.get(ch, 0), ctr[ch])
        for word in words1:
            ctr = Counter(word)
            uni = True
            for ch in count_dict:
                if ctr.get(ch, 0) < count_dict[ch]:
                    uni = False
                    break
            if uni:
                res.append(word)
        return res
