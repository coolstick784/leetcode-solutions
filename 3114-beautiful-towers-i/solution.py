# for each possible peak, we have a right cost and a left cost
# at each point, if it is the peak, what is the cost to the left and the right? total sum - right cost - left cost = ans
# for the first index, the left cost is obviously 0
# for each index after that, we do o(n^2) where we loop through everything before it, and if it's greater than it, we subtract the difference
# but if it's greater than the previous element we do nothing

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        left_costs = [0 for _ in heights]
        right_costs = [0 for _ in heights]

        left_heights = heights.copy()
        right_heights = heights.copy()
        cur_cost = 0
        for idx in range(len(heights)):
            n = left_heights[idx]
            
            if idx == 0:
                continue

            
            for idx2, height in enumerate(left_heights[:idx]):
                if height > n:
                    cur_cost += height - n
                    left_heights[idx2] = n
            left_costs[idx] = cur_cost

        cur_cost = 0
        for idx in range(len(heights)-2, -1, -1):
            n = right_heights[idx]


            
            for idx2, height in enumerate(right_heights[idx+1:]):
                if height > n:
                    cur_cost += height - n
                    right_heights[idx+idx2+1] = n
            right_costs[idx] = cur_cost
        
        min_cost = float('inf')
        for idx in range(len(heights)):
            min_cost = min(min_cost, left_costs[idx] + right_costs[idx])

        return sum(heights) - min_cost
