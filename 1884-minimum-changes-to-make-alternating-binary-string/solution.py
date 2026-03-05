class Solution:
    def minOperations(self, s: str) -> int:

        # At each element, we want the minimum cost where A. the element ends at 1 and it's alternating and 
        # B. the element ends at 2 and is alternating 
        # Then, we go to the next element, and 
        # A. the min cost at 0 is min_cost_1 + 1 if the el is 1, min_cost_0 if the el is 0
        # B. the min cost at 1 is flipped
    

        if len(s) == 1:
            return 0
        if s[0] == "0":
            min_cost_0 =0
            min_cost_1 = 1
        else:
            min_cost_0 = 1
            min_cost_1 = 0
        for ch in s[1:]:
            if ch == "0":
                tmp = min_cost_1
                min_cost_1 = min_cost_0 + 1
                min_cost_0 = tmp
            else:
                tmp = min_cost_0
                min_cost_0 = min_cost_1 + 1
                min_cost_1 = tmp

        return min(min_cost_0, min_cost_1)

        
