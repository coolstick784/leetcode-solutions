MOD = 10**9+7
@lru_cache(None)
def solve(curN, curK):
    if curK == 0:
        return 1
    if curK == 1:
        return curN
    if curN == 1:
        return 1
    if curN == 2:
        return curK + 1
    return (solve(curN, curK-1) + solve(curN-1, curK)) % MOD

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:



        return solve(n, k) % MOD
