class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        ctr = Counter(nums)
        if len(nums) % k != 0:
            return False
        groups = len(nums) // k
        return max(ctr.values()) <= groups
