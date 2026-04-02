class Solution:
    def twoEggDrop(self, n: int) -> int:
        # we need to find the optimal number for the first egg 
        # if the first egg breaks, we just move down by 1 with the second until we find it
        # we want the maximum value for if either A. the first egg breaks or B. the first egg doesnt break
        # where do we drop the first egg?
        # if we have less, we go closer to 1/2
        # 3: 1
        # 4: 2
        # 5: 3
        # 6: 3/4
        # 7: 

        # i is if the first one breaks, if it's doesn't break we have n - i
        @lru_cache(None)
        def solve(num):
            if num == 1:
                return 1

            return min([max(i, 1+solve(num-i)) for i in range(1, num)])
        return solve(n)

