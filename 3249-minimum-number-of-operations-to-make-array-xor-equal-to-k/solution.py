class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cur = 0
        for n in nums:
            cur = cur ^ n
        need = cur ^ k
        return need.bit_count()
