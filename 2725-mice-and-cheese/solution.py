class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        cost = [(reward2[idx] - reward1[idx], idx) for idx in range(len(reward1))]
        cost.sort()
        idxs = set([v[1] for v in cost[:k]])
        res = 0
        for idx, n in enumerate(reward1):
            if idx in idxs:
                res += n
            else:
                res += reward2[idx]
        return res
