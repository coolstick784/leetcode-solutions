class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        for l in range(k, len(s)+1):
            res = None
            left = 0
            right = 0
            ct = 0
            while right < len(s):
                #print("left", left, "right", right)
                ch = s[right]
                if ch == "1":
                    ct += 1
                if right - left + 1 == l:
                    
                    if ct == k:
                        if res is None:
                            res = s[left:right+1]
                        else:
                            res = min(res, s[left:right+1])
                    prev_ch = s[left]
                    if prev_ch == "1":
                        ct -= 1
                    left += 1

                right += 1
            if res is not None:
                return res

        return ""
