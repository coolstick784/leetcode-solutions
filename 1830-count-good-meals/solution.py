class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pows = [2 ** n for n in range(32)]
        explored = {}
        res = 0
        for idx, n in enumerate(deliciousness):
            for p in pows:
                goal = p - n
                res += explored.get(goal, 0)
            explored[n] = explored.get(n, 0) + 1
        return res % (10**9 + 7)
