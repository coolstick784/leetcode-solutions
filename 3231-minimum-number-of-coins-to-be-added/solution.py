
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        ctr = Counter(coins)
        res = []
        out = 0
        s = 0
        for n in range(1, target+1):
            s += ctr.get(n, 0) * n
            if s < n:
                out += 1
                s += n
        return out
