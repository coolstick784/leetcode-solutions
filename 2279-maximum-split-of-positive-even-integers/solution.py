class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        start = 2
        cur = finalSum
        res = []
        while start < cur // 2:
            res.append(start)
            cur -= start 
            start += 2

        res.append(cur)
        return res
