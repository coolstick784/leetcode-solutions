# if < target, move right
# if >, move left
# if equal, return left and right


# [1, 2, 3, 4, 7] # 6
# 0, 1
# 1, 4

# [1, 2, 5, 7, 11, 15] # 7
# 
# while >, move right to the left, then move left to the right until it's greater than
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right and left < len(numbers) and right < len(numbers):
            l = numbers[left]
            r = numbers[right] 
            if l + r == target:
                return [left+1, right+1]
            if l + r > target:
                right -= 1
            else:
                left += 1
    
