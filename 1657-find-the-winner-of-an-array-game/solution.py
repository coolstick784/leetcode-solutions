# we want to ask 2 questions
# 1. is it the greatest up to that point?
# 2. is it either A. the first element and greater than the next k elements, B. in the last k elements and the greatest in the entire array? or C. greater than the next k-1 elements?
# if so, that's our res
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_val = max(arr)
        left = 0
        cur_wins = 0
        cur_champ = -1
        while left < len(arr):
            val = arr[left]
            if val == max_val:
                return val
            if left == 0:
                cur_champ = val
            else:
                if val > cur_champ:
                    cur_champ = val
                    cur_wins = 1
                else:
                    cur_wins += 1
            if cur_wins == k:
                return cur_champ
            left += 1


        
