class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

            
        @lru_cache(10**5)
        def solve(start, end, turn):
            if start > end:
                return 0

            if turn:

                return max(solve(start+1, end, False), solve(start, end-1, False))
            else:
                return min(stones[start] + solve(start+1, end, True), stones[end] + solve(start, end-1, True))


            
        



        
        return solve(0, len(stones) - 1, True)
