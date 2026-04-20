# we want to know all numbers we're looking for, and the number we need left in each grouping
# so we can create a dictionary for each number that we need, and a list of the groups we need (really just need the # left)
# so each number can be associated with a stack

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        nums = {}
        for idx, n in enumerate(hand):
            if nums.get(n, []) != []:
                need = nums[n].pop() - 1
            else:
                need = groupSize - 1
            if need != 0:
                nums.setdefault(n+1, []).append(need)


        for n in nums:
            if nums[n] != []:
                return False
        return True
