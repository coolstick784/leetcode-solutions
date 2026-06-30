# basically, we can either keep or swap the last element
# if we keep, we need to swap all the elements in nums1 greater than it

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:


        def solve(n1, n2):
            out = 0
            for idx, n in enumerate(nums1):
                n2n = nums2[idx]
                if n > n1:
                    out += 1
                    if n2n > n1 or n > n2:
                        return float('inf')
                elif n2n > n2:
                    out += 1
                    if n > n2 or n2n > n1:
                        return float('inf')
            return out


        res = min(solve(nums1[-1], nums2[-1]), solve(nums2[-1], nums1[-1]))
        return res if res != float('inf') else -1 
        
