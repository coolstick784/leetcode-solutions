class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def similar(w1, w2):
            changes = 0
            for idx, ch in enumerate(w1):
                if ch != w2[idx]:
                    changes += 1
                if changes > 2:
                    return False
            return True


        res = []
        for q in queries:
            for w in dictionary:
                if similar(q, w):
                    res.append(q)
                    break
        return res
