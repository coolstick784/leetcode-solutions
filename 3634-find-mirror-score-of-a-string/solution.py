class Solution:
    def calculateScore(self, s: str) -> int:
        res = 0
        mirrors = {}
        for ch in set(s):
            mirrors[ch] = chr(ord('z') - (ord(ch) - ord('a')))
        print(mirrors)
        stack = {}
        for idx, ch in enumerate(s):
            m = mirrors.get(ch, "")
            if m in stack and stack[m]:
                
                res += idx - stack[m].pop()

              
            else:
                stack.setdefault(ch, []).append(idx)
        return res


