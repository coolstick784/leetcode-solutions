class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = []

        for idx, n in enumerate(nums):
            if n >= 0:
                pos.append(idx)

        if not pos:
            return nums

        rotated = [None for _ in pos]

        for idx, p in enumerate(pos):
            rotated[(idx - k) % len(pos)] = p

        r_idx = 0
        res = []

        for idx, n in enumerate(nums):
            if n < 0:
                res.append(n)
            else:
                res.append(nums[rotated[r_idx]])
                r_idx += 1

        return res
