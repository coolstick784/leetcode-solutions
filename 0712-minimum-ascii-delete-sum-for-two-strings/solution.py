class Solution(object):
        
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1 = list(s1)
        s2 = list(s2)
        def getSum(chars):
            cur_sum = 0
            for ch in chars:
                cur_sum += ord(ch)
            return cur_sum
        dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
        for idx, ch2 in enumerate(s2):
            if s1[-1] in s2[idx:]:
                dp[idx][len(s1)-1] = getSum(s2[idx:]) - ord(s1[-1])
            else:
                dp[idx][len(s1)-1] = getSum(s2[idx:]) + ord(s1[-1])
        for idx, ch1 in enumerate(s1):
            if s2[-1] in s1[idx:]:
                dp[len(s2)-1][idx] = getSum(s1[idx:]) - ord(s2[-1])
                #print(s1[idx:])
                #print(getSum(s1[idx:]))
                #print( getSum(s1[idx:]) - ord(s2[-1]))
            else:
                dp[len(s2)-1][idx] = getSum(s1[idx:]) + ord(s2[-1])
        for row in range(len(s2)-2, -1, -1):
            for col in range(len(s1)-2, -1, -1):
                bottom_right = dp[row+1][col+1]
                right = dp[row][col+1]
                bottom = dp[row+1][col]
                cur_s2_ch = s2[row]
                cur_s1_ch = s1[col]
                
                if cur_s2_ch == cur_s1_ch:
                    dp[row][col] = min(bottom_right, right + ord(cur_s1_ch), bottom + ord(cur_s2_ch))
                else:
                    dp[row][col] = min(right + ord(cur_s1_ch), bottom + ord(cur_s2_ch))
        return dp[0][0]


