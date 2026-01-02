class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        while idx1 < len(nums1):
            if idx2 >= len(nums2):
                pass
            elif nums1[idx1] == 0 and max(nums1[idx1:]) == 0:
                nums1[idx1] = nums2[idx2]
                idx2 += 1

            elif nums2[idx2] < nums1[idx1]:
                nums1.pop()
                
                print("insrting", nums2[idx2])
                nums1.insert(idx1, nums2[idx2])
                
                idx2 += 1
            print("nums1", nums1)
            idx1 += 1
