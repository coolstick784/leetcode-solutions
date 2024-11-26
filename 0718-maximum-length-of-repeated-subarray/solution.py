class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n_rows = len(nums2)
        n_cols = len(nums1)
        dp = [[(0,0) for _ in range(n_cols)] for _ in range(n_rows)]
        for j in range(n_cols):
            if nums2[0] in nums1[:j+1]:
                first = 1
            else:
                first = 0
            if nums2[0] == nums1[j]:
                second = 1
            else:
                second = 0
            dp[0][j] = (first, second)
        for i in range(n_rows):
        
            if nums1[0] in nums2[:i+1]:
                first = 1
            else:
                first = 0
            if nums1[0] == nums2[i]:
                second = 1
            else:
                second = 0
            dp[i][0] = (first, second)
        # i is the row and j is the col
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                cur_max = max(dp[i-1][j][0], dp[i][j-1][0])
                if nums2[i] == nums1[j]:
                    prev_cur = dp[i-1][j-1][1]
                    cur_max = max(cur_max, prev_cur+1)
                    dp[i][j] = (cur_max, prev_cur+1)
                else:
                    dp[i][j] = (cur_max, 0)

        return dp[n_rows-1][n_cols-1][0]
