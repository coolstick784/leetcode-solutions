class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # For each starting point, have a running minimum
        # If that minimum is < the current minimum, multiply the minimum by the number it is less than. No need to double count
        # e.g. for [3,1,2,4]
        # [3] (3) -> 1 is lower than, so start with 1 -> [1] *2 (5) -> [1, 2] (7) -> [1, 2, 4] (9) -> 3 + 6 -> [2] (11) -> [2, 4] (13) -> [4] (17)
        # We want all the local minimums up to the current point, and add them from the difference to the current point + 1
        # If the current value is > all local minimums added so far, add it
        # If it's less than any of them, insert it and remove any > it
        res = 0
        # val, idx, diff from last local min
        local_mins = []
        cur_sum = 0

        
        for left in range(0, len(arr)):
            cur = arr[left]
            diff = 1
            #while local_mins and neg_cur > local_mins[0][0]:
            while local_mins and local_mins[-1][0] >= cur:
                last_val, last_idx, last_diff = local_mins.pop()
                diff += last_diff
                cur_sum -= last_val * last_diff  # remove popped contribution
                
            local_mins.append((cur, left, diff))
  
            cur_sum += cur * diff

            # All subarrays ending at 'left' contribute cur_sum
            res += cur_sum



        return res % (10**9+7)
