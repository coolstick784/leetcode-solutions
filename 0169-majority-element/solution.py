# [2, 1, 2,2,1, 1, 1, 2, 2]

# y, y-1
 #(y-x), x

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        largest, ct = -float('inf'), 1
        for n in nums:
            if n == largest:
                ct += 1
            else:
                ct -= 1
            if ct == 0:
                largest = n
                ct = 1
        return largest
