# we want a stack
# if the asteroid is positive, add it to the stack
# if it is negative, compare it to each asteroid in the stack
# if it's > the abs value, remove the asteroid from the stack
# if the stack is empty, add the negative asteroid to the solution
# if they're equal, remove 1 from the stack and move the asteroi index to the right one
# once we've reached the end, add the stack to the resolution

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = []
        for idx, a in enumerate(asteroids):
            if a > 0:
                stack.append(a)
            elif a < 0:
                abs_a = abs(a)
                while stack and stack[-1] < abs_a:
                    stack.pop()
                if stack and stack[-1] == abs_a:
                    stack.pop()
                elif stack == []:
                    res.append(a)
        res += stack
        return res
