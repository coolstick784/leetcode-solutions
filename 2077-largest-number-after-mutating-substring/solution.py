class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        res = []
        started = False
        done = False
        for idx, n in enumerate(num):
            n = int(n)
            if change[n] > n and not done:
                res.append(change[n])
                started = True
            
            elif change[n] < n:
                if started:
                    done = True
                res.append(n)
            else:
                res.append(n)


        return "".join([str(n) for n in res])
