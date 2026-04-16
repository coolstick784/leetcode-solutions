# so for each right idx, we want to ask what's the minimum number of excess Rs or Ls we need to create a balanced string at this element?
# "RLRRRLLRLL"
# so we basically need to keep in mind how many Rs or Ls we need 
# if it's 0, add 1 to res and move on



class Solution:
    def balancedStringSplit(self, s: str) -> int:
        need = [1, 1]
        idx = 0
        res = 0
        while idx < len(s):
            cur = s[idx]
            if cur == "L":
                if need[0] == 0:
                    need[1] += 1
                else:
                    need[0] -= 1
            else:
                if need[1] == 0:
                    need[0] += 1
                else:
                    need[1] -= 1
            if need == [0, 0]:
                res += 1
                need = [1, 1]
            idx += 1
        return res
