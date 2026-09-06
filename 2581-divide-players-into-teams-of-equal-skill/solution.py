from collections import Counter
import math
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ctr = Counter(skill)
        group = sum(skill) / (len(skill))
        group *= 2
        group = int(group)
   
        res = 0
        for n in range(1, math.ceil(group/2)):
            m = group - n
            if ctr.get(m, 0) != ctr.get(n, 0):
                print("m", m, "n", n, "bad")
                return -1
            res += (m*n) * ctr.get(n, 0)
            print("n", n, "m", m, "add", (m*n) * ctr.get(n, 0))
        if group % 2 == 0 and ctr.get(group//2, 0) % 2 == 1:
            
            return -1
        elif group % 2 == 0:
            n = group//2
            res += ctr.get(n, 0) // 2 * n * n
        return res


