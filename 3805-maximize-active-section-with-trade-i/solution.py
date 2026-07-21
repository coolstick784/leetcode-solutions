# either 1. convert a group to 0s then convert that group or 
# 2. convert the smallest 1 group then the largest 0 group


# there must be a section of 1s -> 0s -> 1s -> 0s -> 1s, and we then add the 2 0s
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s = '1' + s + '1'
        base = Counter(s)['1']
        cur_ch = None
        cur_ct = 0
        rows = []
        for idx, ch in enumerate(s):
            if ch == cur_ch:
                cur_ct += 1
            else:
                if cur_ch:
                    rows.append((cur_ch, cur_ct))
                cur_ch = ch
                cur_ct = 1
        rows.append((cur_ch, cur_ct))

        combined = 0
        separate_min = float('inf')
        separate_max = 0

        for idx, (ch, ct) in enumerate(rows):
            if idx < len(rows)-4:
                five = [ch, rows[idx+1][0], rows[idx+2][0], rows[idx+3][0], rows[idx+4][0]]
                if five == ['1', '0', '1', '0', '1']:
                    combined = max(combined, rows[idx+1][1] + rows[idx+3][1])
            if idx < len(rows) - 2:
                three = [ch, rows[idx+1][0], rows[idx+2][0]]
                if three == ['1', '0', '1']:
                    separate_max = max(separate_max, rows[idx+1][1])
                elif three == ['0', '1', '0']:
                    separate_min = min(separate_min, rows[idx+1][1])
        
        return base + max(combined, separate_max - separate_min) - 2


                
