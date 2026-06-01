class Solution:
    def countOfAtoms(self, formula: str) -> str:
        mp = {}
        stack = []
        for idx, ch in enumerate(formula):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                mp[stack.pop()] = idx

        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        letters = [chr(ord('A') + ch) for ch in range(26)]
        low = [l.lower() for l in letters]

        def solve(left, right, multiplier):

            cur = {}
            cur_el = []
            
            if left > right or left >= len(formula):
                return cur
          
            if formula[left] == "(":
                start = left+ 1
                end = mp[left]-1
                digit = 1
                idx = end + 2
                cur_digits = []
                while idx < len(formula) and formula[idx] in digits:
                    cur_digits.append(formula[idx])
                    idx += 1
                if cur_digits:
                    digit = int("".join(cur_digits))
                new = solve(start, end, digit) 
                after = solve(idx, right, 1)
                for item in after:
                    new[item] = new.get(item, 0) + after[item]
                for item in new:
                    new[item] *= multiplier
                return new
            if formula[left] in letters:
                cur_el.append(formula[left])
                left += 1
                while left < len(formula) and formula[left] in low:
                    cur_el.append(formula[left])
                    left += 1
                el = "".join(cur_el)
                digit = 1
                cur_digits = []
                while left < len(formula) and formula[left] in digits:
                    cur_digits.append(formula[left])
                    left += 1
                if cur_digits:
                    digit = int("".join(cur_digits))
                cur[el] = cur.get(el, 0) + digit
                after = solve(left, right, 1)
                for item in after:
                    cur[item] = cur.get(item, 0) + after[item]
                for item in cur:
                    cur[item] *= multiplier
                


                return cur
            return cur
        

        ctr = solve(0, len(formula) - 1, 1)
        res = []
        for el in sorted(ctr.keys()):
            res.append(el)
            if ctr[el] > 1:
                res.append(str(ctr[el]))
        return "".join(res)
        

      
