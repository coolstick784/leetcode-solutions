class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        all_ctr = Counter(s)
        ctr = {}
        ranges = {}
        for idx, ch in enumerate(s):
            if not ranges.get(ch):
                ranges[ch] = [idx, idx]
            else:
                ranges[ch][1] = idx
            ctr.setdefault(idx, {})
            ctr[idx][ch] = ctr.get(idx-1, {}).get(ch, 0) + 1
            for c in ctr.get(idx-1, {}):
                if c == ch:
                    continue
                ctr[idx][c] = ctr.get(idx-1, {}).get(c, 0)
  
        lefts = []
        rights = []
        cur_right = 0
        p = [(ranges[ch][1], ch) for ch in ranges]
        p.sort()
        def possible(left, right):
            for ch in ctr.get(right, {}):
                diff = ctr.get(right, {}).get(ch, 0) - ctr.get(left-1, {}).get(ch, 0) 
                print("left", left, "right", right, "ch", ch, "diff", diff)
                if diff != 0 and diff != all_ctr[ch]:
                    return False
            return True
        all_lefts = [ranges[ch][0] for ch in ranges]
        all_lefts.sort()
        all_lefts = deque(all_lefts)
        p_left = []
        for r, ch in p:
            print("r", r, "all lefts", all_lefts)
            while all_lefts and all_lefts[0] <= r:
                p_left.append(all_lefts.popleft())
            print("p left", p_left)
            for l in p_left:
                if l < cur_right:
                    continue
                if possible(l, r):
                    lefts.append(l)
                    rights.append(r)
                    cur_right = r + 1
                    continue



        res = []
        for idx, l in enumerate(lefts):
            res.append(s[l:rights[idx]+1])
        return res
             
