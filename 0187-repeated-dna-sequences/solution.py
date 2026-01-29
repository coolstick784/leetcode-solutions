class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        right = 10
        all_substr = set()
        res = set()
        while right <= len(s):
            cur_letters = s[left:right]
            if cur_letters in all_substr:
                res.add(cur_letters)
            all_substr.add(cur_letters)

            left += 1
            right += 1
        return list(res)
        
