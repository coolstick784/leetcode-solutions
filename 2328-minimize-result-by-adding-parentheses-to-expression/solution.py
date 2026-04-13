class Solution:
    def minimizeResult(self, expression: str) -> str:
        left_final = 0 # the idx we're going to place it before
        right_final = len(expression)-1 # the idx we're going to place it after
        split_plus = expression.split("+")
        res = float("inf")
        for left_idx in range(len(split_plus[0])):
            for right_idx in range(len(split_plus[1])):
                if left_idx == 0:
                    left_multiplier = 1
                else:
                    left_multiplier = int(split_plus[0][:left_idx])
                if right_idx == len(split_plus[1]) - 1:
                    right_multiplier = 1
                else:
                    right_multiplier = int(split_plus[1][right_idx+1:])
                middle = int(split_plus[0][left_idx:]) + int(split_plus[1][:right_idx+1])
                cur = middle * left_multiplier * right_multiplier
                if cur < res:
                    res = cur
                    left_final = left_idx
                    right_final = right_idx
        return split_plus[0][:left_final] + "(" + split_plus[0][left_final:] + "+" + split_plus[1][:right_final+1] + ")" + split_plus[1][right_final+1:]
                    

