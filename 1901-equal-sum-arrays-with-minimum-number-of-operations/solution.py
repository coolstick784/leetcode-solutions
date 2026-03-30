class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1): return -1 # impossible 
        
        if sum(nums1) < sum(nums2): nums1, nums2 = nums2, nums1
        s1, s2 = sum(nums1), sum(nums2)
            
        nums1 = [-x for x in nums1] # max-heap 
        heapify(nums1)
        heapify(nums2)
        
        ans = 0
        while s1 > s2: 
            x1, x2 = nums1[0], nums2[0]
            if -1-x1 > 6-x2: # change x1 to 1
                s1 += x1 + 1
                heapreplace(nums1, -1)
            else: 
                s2 += 6 - x2
                heapreplace(nums2, 6)
            ans += 1
        return ans 
