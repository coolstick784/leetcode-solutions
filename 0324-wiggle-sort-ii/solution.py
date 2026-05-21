class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = sorted(nums)
        # len(3) -> 1
        # len(4) -> 1
        left = math.ceil(len(new)/2) - 1
        right = len(new) - 1
        idx = 0
        while left >= 0:
            nums[idx] = new[left]
            if idx +1 < len(nums):
                nums[idx+1] = new[right]

            idx += 2
            left -= 1
            right -= 1
