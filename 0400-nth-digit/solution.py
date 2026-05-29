import bisect

class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = [1, 10]
        for _ in range(32):
            nums.append(nums[-1] * 10)
        digits = [1]

        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            numbers = num - nums[idx-1]
            digits.append(numbers * idx + digits[-1])
        
        idx = bisect.bisect(digits, n) - 1
        starting = nums[idx]
        starting_digit = digits[idx]
        num_digits = idx+1
        
        new_n = starting + (n-starting_digit) // num_digits
        n_idx = (n - starting_digit) % num_digits
        return int(str(new_n)[n_idx])
