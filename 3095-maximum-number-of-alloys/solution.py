class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0
        def solve(comp):
            nonlocal budget
            left = 0
            right = 10**9 

            while left < right:
                med = (left + right) // 2 + 1
                money = budget
                for idx, metal in enumerate(comp):
                
                    money -= max(0, ((med * metal) - stock[idx]) * cost[idx])
                    
                    if money < 0:
                        break
         
                if money < 0:
                    right = med - 1
                else:
                    left = med
            
            return left


        for m in range(k):
            
            res = max(res, solve(composition[m]))
           
        return res


