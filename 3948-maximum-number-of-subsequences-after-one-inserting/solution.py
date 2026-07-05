class Solution:
    def numOfSubsequences(self, s: str) -> int:
        new = []
        for idx, ch in enumerate(s):
            if ch not in ['L', 'C', 'T']:
                continue
            new.append(ch)
        base = 0
        add = 0
        try2 = 0
        try3 = 0
        Ls_before = 0
        Ts_after = Counter(s)['T']
        for idx, ch in enumerate(new):
            if ch == 'T':
                Ts_after -= 1
            elif ch == 'L':
                Ls_before += 1
            else:
                base += Ts_after * Ls_before
                try2 += Ts_after * (Ls_before+1)
                try3 += (Ts_after+1) * Ls_before
            add = max(add, Ts_after * Ls_before)


        return max(base + add, try2, try3)
