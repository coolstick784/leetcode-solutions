class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        goal = nums2[-1]
        res = 0
        last = float('inf')
        for idx, n in enumerate(nums1):
            n2 = nums2[idx]
            if n >= n2:
                if goal <= n and goal >= n2:
                    last = 1
                res += (n-n2)
            else:
                if goal >= n and goal <= n2:
                    last = 1
                res += (n2-n)
            last = min(last, abs(n-goal)+1, abs(n2-goal)+1)

        return res + last
