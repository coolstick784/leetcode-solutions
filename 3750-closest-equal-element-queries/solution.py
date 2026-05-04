class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        idxs = {}
        for i, num in enumerate(nums):
            idxs.setdefault(num, []).append(i)

        res = []

        for idx in queries:
            num = nums[idx]
            arr = idxs[num]

            if len(arr) == 1:
                res.append(-1)
                continue

            pos = bisect.bisect_left(arr, idx)

            left = arr[pos - 1]
            right = arr[(pos + 1) % len(arr)]

            d1 = abs(idx - left)
            d2 = abs(idx - right)

            res.append(min(d1, n - d1, d2, n - d2))

        return res
