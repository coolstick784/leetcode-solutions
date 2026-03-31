from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        need = {}

        for n in nums:
            if count[n] == 0:
                continue

            count[n] -= 1

            if need.get(n, 0) > 0:
                need[n] -= 1
                need[n + 1] = need.get(n + 1, 0) + 1

            elif count.get(n + 1, 0) > 0 and count.get(n + 2, 0) > 0:
                count[n + 1] -= 1
                count[n + 2] -= 1
                need[n + 3] = need.get(n + 3, 0) + 1

            else:
                return False

        return True
