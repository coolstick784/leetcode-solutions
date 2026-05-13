# add it left to right, and then look back after completing our addition

# ask, for an element, is it equal to its previous value?
# if so, combine the two, then look left again
# keep doing that until it's not equal to previous
# then, move the index right one

# so we'll iterate with a left and right index
# the left index indicates we've moved through everything through the left but not including
# we want to explore everythign to the right and beyond
# we'll have a set of indices we want to remove, so we edit in place, and then we loop over it again at the end to remvoe the ones we want to remove

# [3, 1, 1, 2] left = 0 right = 1
# [3, 1, 1, 2] left = 1 right = 

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        to_remove = set()
        left = 0
        right = 1
        while left < len(nums) and right < len(nums):
            if nums[right] == nums[left]:
                nums[left] += nums[right]
                
                while left > 0 and nums[left-1] == nums[left]:
                    to_remove.add(left)
                    nums[left-1] *= 2
                    left -= 1
            else:
                nums[left+1] = nums[right]

                left += 1

            to_remove.add(right)
            if left in to_remove:
                to_remove.remove(left)
            right += 1
        res = []
        for idx, n in enumerate(nums):
            if idx not in to_remove:
                res.append(n)
        return res        
