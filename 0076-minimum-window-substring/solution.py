class Solution:
    def minWindow(self, s: str, t: str) -> str:
        base = Counter(t)
        need = len(t)
        left = 0
        right = 0 
        res = float('inf')
        best_start = -1
        best_end = -1
        print("base", base)
        while right < len(s):
            found = False
            while right < len(s) and need > 0:
                ch = s[right]
                if ch in base:
                    base[ch] -= 1
                    if base[ch] >= 0:
                        need -= 1
                if need == 0:
                    found = True
                print("left", left, "right", right, "ch", ch, "need", need)
                right += 1
            while left < right and need == 0:
                ch = s[left]
                if ch in base:
                    base[ch] += 1
                if base[ch] > 0:
                    need += 1
                left += 1
            print("left", left-1, "right", right-1, "need", need)
            if found:
                cur = (right-1) - (left-1) + 1
                if cur < res:
                    res = cur
                    best_start = left - 1
                    best_end = right - 1


        if res == float('inf'):
            return ""
        return s[best_start:best_end + 1]
