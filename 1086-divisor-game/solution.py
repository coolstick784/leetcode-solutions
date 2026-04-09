# if n = 1, the player whose turn it is loses
# if n = 2, the player whose turn it is wins
# if n = 3, the player whose turn it is loses
# if n = 4, the player whose turn it is wins
# if n = 5, the player whose turn it is wins

# so basically, we're looking for every factor of n
# if n = 1, it's a loss
# so for each factor of n, we subtract n - x from it, and we have the opposite
# if any of the opposites are a win, return win
# otherwise, return lose

class Solution:
    @lru_cache(None)
    def divisorGame(self, n: int) -> bool:
        @lru_cache(None)
        def get_factors(num):
            out = []
            for i in range(1, num//2+1):
                if num % i == 0:
                    out.append(i)
            return out
        
        
        if n == 1:
            return False
        
        
        for factor in get_factors(n):
            if not self.divisorGame(n - factor):
                return True
        return False
