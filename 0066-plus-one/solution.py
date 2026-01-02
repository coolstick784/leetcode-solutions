class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_idx = len(digits) - 1
        while cur_idx >= 0:
            digits[cur_idx] += 1
            if digits[cur_idx] != 10:
                return digits
            if cur_idx != 0:
                digits[cur_idx] = 0
            cur_idx -= 1
        if digits[0] == 10:
            digits.insert(0, 1)
            digits[1] = 0
        return digits
