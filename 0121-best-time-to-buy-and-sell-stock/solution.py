class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start at the left, go to the right
        # If right > left, max_difference = max(max_difference, right - left)
        # If right < left, left = right
        max_difference = 0
        left = 0
        right = 0
        while right < len(prices):

            if prices[right] > prices[left]:

                max_difference = max(max_difference, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_difference
