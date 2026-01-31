class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        lowest = [2**31-1 for _ in range(3)]
        highest = [-2**31 for _ in range(3)]
        for n in nums:
            if n < lowest[2]:
                lowest[0] = lowest[1]
                lowest[1] = lowest[2]
                lowest[2] = n
            elif n < lowest[1]:
                lowest[0] = lowest[1]
                lowest[1] = n
            elif n < lowest[0]:
                lowest[0] = n
            if n > highest[2]:
                highest[0] = highest[1]
                highest[1] = highest[2]
                highest[2] = n
            elif n > highest[1]:
                highest[0] = highest[1]
                highest[1] = n
            elif n > highest[0]:
                highest[0] = n

        # can do left, right, left left, right right
        # lowest[0] is the 3rd lowest, lowest[1] is the 2nd lowest, lowest[2] is the lowest
        # highest[0] is the 3rd highest, highest[1] is the 2nd highest, highest[2] is the highest
        print("highest", highest)
        print("lowest", lowest)
        
        return min([highest[1] - lowest[1], highest[2] - lowest[0], highest[0] - lowest[2]])
        
