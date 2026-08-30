from collections import deque
class Solution:
    def smallestNumber(self, num: int) -> int:

        if num == 0:
            return 0
        res = []
        if num > 0:
            num = deque(sorted(list(str(num))))
            num_zeros = 0
            while num[0] == "0":
                num_zeros += 1
                num.popleft()
            res.append(num.popleft())
            for _ in range(num_zeros):
                res.append("0")
            res += list(num)
            return int("".join(res))
        num = str(-1 * num)
        num = sorted(list(num))
        num.reverse()
        return -1 * int("".join(num))
        
    
