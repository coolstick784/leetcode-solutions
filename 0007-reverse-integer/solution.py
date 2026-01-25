class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            start = "-"
        else:
            start = ""
        x = abs(x)
        as_l = list(str(x))
        compare = 2**31
        as_l.reverse()
        as_str_no_sign =  "".join(as_l)
        as_str = start + as_str_no_sign
        def outOfRange(cur, compare):
            if start == "-":
                neg = True
            else:
                neg = False
            
            comp_str = list(str(compare))
            if len(cur) > len(comp_str):
                return True
            if len(cur) < len(comp_str):
                return False
            for idx, ch in enumerate(cur):
                cur_comp = int(comp_str[idx])
                if idx == len(cur) - 1 and neg==False:
                    cur_comp -= 1
                
                if int(ch) < cur_comp:
                    return False
                elif int(ch) == cur_comp and idx == len(cur) - 1:
                    return False
                elif int(ch) > cur_comp:
                    return True
            return True

        if outOfRange(as_str_no_sign, compare):
            return 0
        else:
            return int(as_str)
        
