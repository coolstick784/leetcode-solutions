class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = [0]
        csum = [0]
        for m, c in enumerate(customers):
            if not grumpy[m]:
                satisfied.append(satisfied[-1] + c)
            else:
                satisfied.append(satisfied[-1])
            csum.append(csum[-1] + c)
        
           
        res = 0
        for m in range(len(customers)):
            start = m
            end = min(len(customers), start+minutes)
            res = max(res, satisfied[m] + csum[end] - csum[start] + satisfied[-1] - satisfied[end])
        return res 
