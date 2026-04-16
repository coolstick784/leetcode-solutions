# at each index, we want the distance to the person closest to the left and the distance to the person closest on the right
# take the min of those 2 values at each
# the max of those mins is our answer

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = []
        right = []
        past_left = -1*float("inf")
        past_right = float("inf")
        for idx, s in enumerate(seats):
            if s == 1:
                left.append(0)
                past_left = idx
            else:
                left.append(idx - past_left)
        for idx in range(len(seats)-1, -1, -1):
            s = seats[idx]
            if s == 1:
                right.append(0)
                past_right = idx
            else:
                right.append(past_right - idx)
        right.reverse()
        res = 0
        for idx in range(len(seats)):
            res = max(res, min(right[idx], left[idx]))
        return res
