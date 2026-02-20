class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # If there aren't any matches, make it smaller
        # If there are matches, make it bigger
        res = 1
        left = 0
        right = 0
        ctr = {}
        moved_out = True
        for n in range(26):
            ch = chr(ord('A') + n)
            ctr[ch] = 0
        while left < len(s) and right < len(s):
            if moved_out:
                ctr[s[right]] += 1
            else:
                ctr[s[left-1]] -= 1
            moved_out = False
            for n in range(26):
                ch = chr(ord('A') + n)
                if ctr[ch] >= (right-left-k+1):
                    moved_out = True
            if moved_out:
                res = max(res, right-left+1)
                right += 1
            else:
                left += 1
            
        return res


        
