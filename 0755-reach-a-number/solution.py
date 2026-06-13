# n(n+1) // 2


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        left = 0
        right = target 
        while left < right:
            med = (left + right) // 2
            if med * (med+1) // 2 >= target:
                right = med
            else:
                left = med + 1
        while (left * (left + 1) // 2 - target) % 2 == 1:
            left += 1
        return left
