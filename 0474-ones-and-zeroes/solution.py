# for any two given strings, there are 2 possibilites:
# 1. one has >= 1s and >= 0s than the other
# 2. they have mixed 1s and 0s >


# we are always going to drop the one that brings our score down the most
# 5 1s 5 0s
# 6 1s 4 0s
# 8 1s 3 0s

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        dp[(0, 0)] = 0
        for s in strs:
            ct = Counter(s)
            new_dp = dp.copy()
            for el in dp:
                z = el[0]
                o = el[1]
                if z + ct["0"] <= m and o + ct["1"] <= n:
                    k = (z+ct["0"], o+ct["1"])
                    new_dp[k] = max(dp[(z, o)] + 1, new_dp.get(k, 0))
            dp = new_dp.copy()
        return max(dp.values())
