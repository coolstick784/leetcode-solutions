class Solution:
    def reverseVowels(self, s: str) -> str:
        idxs = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for idx, ch in enumerate(s):
            if ch in vowels:
                idxs.append(idx)
        res = ""
        reversed_idxs = idxs[::-1]
        left = 0

        for idx in range(len(s)):

           
            if left >= len(idxs) or idx < idxs[left]:
                res += s[idx]
            else:
                res += s[reversed_idxs[left]]
                left += 1
        return res
                
