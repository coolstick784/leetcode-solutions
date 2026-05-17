# prev, loop through j, k
# ct current * ct new * ct old

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        res = 0
        prev = {}

        for j in range(len(arr)):
            jn = arr[j]
            for k in range(j+1, len(arr)):
                kn = arr[k]
                goal = target - (jn + kn)
                if goal in prev:
                    res += prev[goal]

            

            prev[jn] = prev.get(jn, 0) + 1
        return res % (10**9+7)
