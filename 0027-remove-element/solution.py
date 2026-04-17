# first, get the count of val in nums
# then, look through the first k elements of nums
# we'll also have a left index starting at index k of everything past k
# so keep checking the l1 index for the val, if it s, check l2 index until it's not val, then swap
# continue until we've reached up to k

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for n in nums:
            if n == val:
                k -= 1
        l1 = 0
        l2 = k
        while l1 < k:
            if nums[l1] != val:
                l1 += 1
                continue
            while nums[l2] == val:
                l2 += 1
            nums[l1], nums[l2] = nums[l2], nums[l1]
            l1 += 1
        
   
        return k
