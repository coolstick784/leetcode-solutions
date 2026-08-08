factors = {}
for num in range(1, 10**5+1):
    for n2 in range(1, math.ceil(math.sqrt(num))+1):
        if num % n2 == 0:
            factors.setdefault(num, []).append(n2)
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        def solve(cur_n, cur_k, mn):
            if cur_k == 0:
                return (mn, [])
            if cur_k == 1 and cur_n >= mn:
                return (cur_n, [cur_n])
            elif cur_k == 1:
                return (float('inf'), [])
            cur_factors = [f for f in factors[cur_n] if f >= mn]
            if not cur_factors:
                return (float('inf'), [])
            out = float('inf')
            best = None
            for f in cur_factors:
                sol, li = solve(cur_n // f, cur_k-1, f)
                if sol < out:
                    out = sol
                    best = [f] + li 
                    print("f", f, "out", out, "best", best)
            return (out, best)

        res = float('inf')
        all_factors = factors[n]
        fin = None
        for f in all_factors:
            sol, li =  solve(n//f, k-1, f)
            print("f", f, "li", li, "sol", sol)
            if sol - f < res:
                
                res = sol - f
                fin = [f] + li
        return fin
            


        
        
