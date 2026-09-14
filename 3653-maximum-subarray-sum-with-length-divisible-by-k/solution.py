class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        starts = [n for n in range(k, 2*k)]
        res = -float('inf')
        #print(pre)
        for s in starts:
            idx = s
            cur = 0
            
            while idx <= len(nums):
                cur = pre[idx] - pre[idx-k] + cur
                res = max(res, cur)
                cur = max(cur, 0)
                #print("start", s, "idx", idx, "cur", cur)
                idx += k
        return res

