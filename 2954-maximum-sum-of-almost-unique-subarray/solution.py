class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ctr = {}
        left = 0
        right = 0
        distinct = 0
        s = 0
        mx = 0
        while right < len(nums):

            length = right - left + 1
            
            r = nums[right]
            ctr[r] = ctr.get(r, 0) + 1
            s += r
            print("prev", s)
            if ctr[r] == 1:
                distinct += 1
            while length > k:
                ctr[nums[left]] -= 1
               
                length -= 1

                s -= nums[left]

                if ctr[nums[left]] == 0:
                    distinct -= 1
                left += 1

            if length == k and distinct >= m:
                mx = max(mx, s)


            right += 1
        return mx
            
