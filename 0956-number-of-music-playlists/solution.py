# at each index, we can either play a song that has reached it cooldown or a new song

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7

        @lru_cache(None)
        def solve(idx, off_cd, cd, left): # the current index, how many are used but off cd, how many are on cd, and the number of songs we still have to play
            if left == 0 and idx == goal:
                return 1
            if idx == goal:
                return 0
            out = 0
            remove = 0
            if cd == k:
                remove = 1
            if off_cd:
                out += off_cd * solve(idx+1, off_cd -1 + remove, cd+1-remove, left)
            if left:
                out += left * solve(idx+1, off_cd + remove, cd+1-remove, left-1)
            return out % MOD
            
            


        return solve(0, 0, 0, n)

