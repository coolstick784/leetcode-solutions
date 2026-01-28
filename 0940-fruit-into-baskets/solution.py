class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # want to find the most trees in a row with fruits of only 2 types
        # if it's e.g. AAABBACCBB, have to start from the first C
        # Want to know:
        # - When the first fruit started
        # - The index of the last time the current fruit was (in a row), e.g. BBAAA, A would be index 2
        # - Where we are now
        # - The numbers of our two fruits
        # - If it's a different fruit from the current two, set the left to be the index of the last time the n-1 fruit started their streak


        left = 0
        cur_max = 0
        older_fruit = -1
        recent_fruit = -1
        last_streak_idx = 0

        for idx, n in enumerate(fruits):
            if n != older_fruit and n != recent_fruit: # a third fruit. Need to update the last streak, last fruit, and start new
                older_fruit = recent_fruit
                left = last_streak_idx
                
                last_streak_idx = idx
            elif n == older_fruit: #add 1 to the total if it's contuining the streak
                older_fruit = recent_fruit
                last_streak_idx = idx
            recent_fruit = n
            cur_max = max(cur_max, idx-left+1)
        return cur_max

