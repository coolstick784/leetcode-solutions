#[1,2,3,4,5,6] k = 4
#[-1,-1,-1,-1,-1,-1]
#[0, 0, 1, 1, -1, -1]
#[-1, 0, 0, 1, 1, -1, -1]
#[-1, -1, 0, 0, 1, 1]
#the one that was the previous left turns into its original, the one that was the leftmost 1 turns into a 0, and the one that was to the right of the last 1 trns into a 1

#prices = [4,2,8], strategy = [-1,0,1], k = 2
# base = 4
# first = 10, prev_left  = 0, leftmost_one = 1, next_right = 2
# cur=6-> 4->-4->4

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = 0
        base = 0
        for idx, s in enumerate(strategy):
            base += s * prices[idx]
        first = 0
        for idx, s in enumerate(strategy):
            if idx < k//2:
                continue
            elif idx < k:
                first += prices[idx]
            else:
                first += s * prices[idx]
        res = max(base, first)
        prev_left = 0
        leftmost_one = k // 2
        next_right = k
        cur = first
        while next_right < len(strategy):
            cur += strategy[prev_left] * prices[prev_left]
            cur -= prices[leftmost_one]
            cur -= strategy[next_right] * prices[next_right]
            cur += prices[next_right]
            res = max(res, cur)

            prev_left += 1
            leftmost_one += 1
            next_right += 1

        return res

