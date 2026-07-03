class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set()
        after2 = set()
        for idx1, n1 in enumerate(nums):
            for idx2 in range(idx1, len(nums)):
                n2 = nums[idx2]
                after2.add(n1 ^ n2)
        for idx1, n1 in enumerate(nums):
            for p in after2:
                res.add(n1 ^ p)


        return len(res)
