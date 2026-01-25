class Solution:
    def myAtoi(self, s: str) -> int:
        

        s = s.strip()
        if s == "":
            return 0
        if s[0] == "-":
            neg = True
            s = s[1:]
        else:
            if s[0] == "+":
                s = s[1:]
            neg = False
        print('s', s)
        first_nonzero_idx = 1000
        first_num_idx = 1000
        first_nonzero_val = 0
        nonzero_nums = [str(n) for n in range(1, 10)]
        nums = [str(n) for n in range(10)]
        last_idx = len(s) - 1
        for idx, ch in enumerate(s):

            if ch in nonzero_nums and idx < first_nonzero_idx:
                first_nonzero_idx = idx
                first_nonzero_val = ch
 
            if ch not in nums :
                if idx <= last_idx:
                    last_idx = idx - 1
                if idx < first_nonzero_idx :
                    return 0
        if last_idx < first_nonzero_idx:
            last_idx = len(s) - 1
        if first_nonzero_val == 0:
            return 0
        print(first_nonzero_idx)
        print(last_idx)
        val = int(s[first_nonzero_idx:last_idx+1])
        if neg:
            val *= -1
        val = max(val, (-2)**(31))
        val = min(val, 2**31-1)
        return val


