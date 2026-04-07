class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # can the whole string before it be decoded, assuming the last one is two digits?
        # if no, return True
        # if yes, return False
        # at each index, we want to ask the question, can either A. up to the 2 characters before it AND the last 2 characters are a bit 
        # or B. up to the character before AND the last character is a bit
        # if yes, then it can be decoded
        
        dp = [True for _ in range(len(bits))]
        for idx, n in enumerate(bits):
            if idx == 0:
                dp[idx] = True
            elif idx == 1:
                if bits[idx-1] == 0:
                    dp[idx] = True
                else:
                    dp[idx] = False
            else:
                if (bits[idx-1] == 0 and dp[idx-1]) or (dp[idx-2] and bits[idx-2] ==1):
                    dp[idx] = True
                else:
                    dp[idx] = False
        last_idx = len(bits)-1
        # if the last one is 0, it's possible to go up to the last one, AND it's impossible for the last two 
        if (bits[last_idx] == 0) and (dp[last_idx]) and (dp[last_idx-1] == False or bits[last_idx-1] == 0):
            return True
        return False
                    
