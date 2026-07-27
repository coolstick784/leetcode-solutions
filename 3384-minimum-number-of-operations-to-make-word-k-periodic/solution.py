class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        ctr = {}
        for idx in range(0, len(word), k):
            s = word[idx:idx+k]
            ctr[s] = ctr.get(s, 0) + 1
        return len(word) // k - max(ctr.values())
