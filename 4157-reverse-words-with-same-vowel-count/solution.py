class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {'a', 'e', 'i','o', 'u'}
        ct = 0
        words = s.split()
        w = words[0]
        for ch in w:
            if ch in vowels:
                ct += 1
        for idx, w in enumerate(words):
            
            if idx == 0:
                continue
            cur_ct = 0
            for ch in w:
                if ch in vowels:
                    cur_ct += 1
            if cur_ct == ct:
                w = list(w)
                w.reverse()
                w = "".join(w)
            words[idx] = w

        return " ".join(words)
