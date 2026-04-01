class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # At each index, we want to know if, ending at that index, what the maximum number of Trues and Falses would be if we replaced k of the opposite
        # We also want to know how many k's we have remaining
        # We can do one loop for True, one loop for False
        # So at each index, we want to know if, ending at that index, how many Trues we would have and how many k's we would have left
        # if we replaced all F's with T up to k times
        # If we have a new T, add 1 to the T counter and don't change k
        # If we have a new F, add 1 to k. if k > k, move our left until we remove a F

        num_true = 0
        left = 0
        right = 0
        cur_k = 0
        while right < len(answerKey):
            ch = answerKey[right]
            if ch == "F":
                cur_k += 1
                while cur_k > k:
                    if answerKey[left] == "F":
                        
                        cur_k -= 1
                    left += 1

            num_true = max(num_true, right-left+1)
            right += 1

        num_false = 0
        left = 0
        right = 0
        cur_k = 0
        while right < len(answerKey):
            ch = answerKey[right]
            if ch == "T":
                cur_k += 1
                while cur_k > k:
                    if answerKey[left] == "T":
                        
                        cur_k -= 1
                    left += 1

            num_false = max(num_false, right-left+1)
            right += 1
        return max(num_true, num_false)
        
