class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        longest = {idx:idx for idx, n in enumerate(nums)}
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n % 2 == nums[idx-1] % 2:
                continue
            longest[idx] = longest[idx-1]
        ans = []
        for start, end in queries:
            if start >= longest[end]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
