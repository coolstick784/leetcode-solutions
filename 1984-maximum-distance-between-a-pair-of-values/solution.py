class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1_idx = 0 
        n2_idx = 0
        res = 0
        while n1_idx < len(nums1) and n2_idx < len(nums2):
            while n1_idx < len(nums1) and nums1[n1_idx] > nums2[n2_idx] and n1_idx < n2_idx:
                n1_idx += 1
            if n1_idx == len(nums1):
                break
            res = max(res, n2_idx - n1_idx)
            n2_idx += 1
        return res
