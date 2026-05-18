class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        cur = 0
        q = 0
        out = 0
        for idx, c in enumerate(customers):
            cur -= runningCost
            q += c
            peopleOn = min(4, q)
            q = max(q-4, 0)
            cur += boardingCost * peopleOn
            if cur > res:
                out = idx + 1 
                res = cur
        t = len(customers)
        while q:
            cur -= runningCost
            peopleOn = min(4, q)
            q = max(q-4, 0)
            cur += boardingCost * peopleOn
            if cur > res:
                out = t + 1
                res = cur
            t += 1
        if res == 0:
            return -1
        return out
