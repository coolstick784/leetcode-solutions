sum_factorial = [1]
for n in range(2, 10**5+1):
    sum_factorial.append(sum_factorial[-1] + n)

import bisect
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return bisect.bisect(sum_factorial, len(grades))
