class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        @lru_cache(None)
        def solve(base_idx, topping_idx, cur_score, num_bought = 0):

            if cur_score > target:
                return (abs(cur_score - target), cur_score)
            diff = abs(cur_score - target)

            best = cur_score
            if topping_idx >= len(toppingCosts):
                return (diff, best)
            if num_bought < 2:
                buy_diff, buy_best = solve(base_idx, topping_idx, cur_score+toppingCosts[topping_idx], num_bought + 1)
               
                if buy_diff == diff:
                    best = min(best, buy_best)
                elif buy_diff < diff:
                    best = buy_best
                    diff = buy_diff
            no_buy_diff, no_buy_best = solve(base_idx, topping_idx+1, cur_score)
            if no_buy_diff == diff:
                best = min(best, no_buy_best)
            elif no_buy_diff < diff:
                best = no_buy_best
                diff = no_buy_diff
            return (diff, best)
            

        
        diff = float('inf')
        best = None
        for base_idx in range(len(baseCosts)):
            cur_diff, s = solve(base_idx, 0, baseCosts[base_idx])
           
        
            if cur_diff == diff:
                best = min(best, s)
            elif cur_diff < diff:
                diff = cur_diff
                best = s


        return best
