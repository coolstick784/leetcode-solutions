class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l_idx = 0
        r_idx = 0
        while l_idx < len(nums1) and r_idx < len(nums2):
            if nums1[l_idx] == nums2[r_idx]:
                return nums1[l_idx]
            if nums1[l_idx] > nums2[r_idx]:
                r_idx += 1
            else:
                l_idx += 1
        return -1
