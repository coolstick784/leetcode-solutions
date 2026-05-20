class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        

        copy = nums.copy()
        for idx, n in enumerate(copy):
            nums[(idx + k) % len(nums)] = n

