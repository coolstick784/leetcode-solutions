class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums_s = set()
        for idx, n in enumerate(nums):
            nums_s.add(n)
        for idx in range(len(moveFrom)):
            f = moveFrom[idx]
            t = moveTo[idx]
            nums_s.remove(f)
            nums_s.add(t)
        return sorted(list(nums_s))

