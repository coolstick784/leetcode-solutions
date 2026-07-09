class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        
        s = sum([num for num in range(1, n+1)])
        if s < abs(target):
            return []
        neg = set()
        
        for num in range(n, 0, -1):
            
            s -= (num*2)
            if s < target:
                s += (num*2)
            else:
                neg.add(num)
        res = []
        
        for num in range(1, n+1):
            if num in neg:
                res.append(-num)
            else:
                res.append(num)

      
        return sorted(res) if sum(res) == target else []

