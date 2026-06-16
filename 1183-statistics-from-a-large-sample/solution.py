class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        s = 0
        ct = sum(count)
        mn = None
        mx = None
        mode = None
        mode_ct = 0
        cur_ct = 0
        median = [0, 0]
        if ct % 2 == 0:
            med_right = ct // 2 + 1
            med_left = ct // 2 
        else:
            med_right = ct // 2 + 1
            med_left = ct // 2 + 1
        for idx, n in enumerate(count):
            s += idx * n
            cur_ct += n
            if mn is None and n:
                mn = float(idx)
            if n:
                mx = float(idx)
            if n > mode_ct:
                mode_ct = n
                mode = float(idx)
            if cur_ct >= med_right and cur_ct - n < med_right:
                median[1] = idx
            if cur_ct >= med_left and cur_ct - n < med_left:
                median[0] = idx
        mean = float(s/ct)
        return [mn, mx, mean, sum(median) / 2, mode]
        
