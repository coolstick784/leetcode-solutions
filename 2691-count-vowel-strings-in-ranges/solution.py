class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pre = [0]
        vowels = set(['a', 'e', 'i','o','u'])
        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])
        ans = []
        for start, end in queries:
            ans.append(pre[end+1] - pre[start])
        return ans
            

