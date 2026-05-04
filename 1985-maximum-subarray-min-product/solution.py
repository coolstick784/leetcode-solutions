class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        left_idxs = [0 for _ in nums]
        right_idxs = [n - 1 for _ in nums]

        stack = []
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                prv_idx = stack.pop()
                right_idxs[prv_idx] = idx - 1
            stack.append(idx)

        stack = []
        for idx in range(n - 1, -1, -1):
            num = nums[idx]
            while stack and nums[stack[-1]] > num:
                prv_idx = stack.pop()
                left_idxs[prv_idx] = idx + 1
            stack.append(idx)

        sums = [0 for _ in nums]
        s = 0
        for idx, num in enumerate(nums):
            s += num
            sums[idx] = s

        res = 0

        for idx, num in enumerate(nums):
            left_sum = sums[left_idxs[idx] - 1] if left_idxs[idx] > 0 else 0
            right_sum = sums[right_idxs[idx]]

            res = max(res, (right_sum - left_sum) * num)

        return res % MOD
