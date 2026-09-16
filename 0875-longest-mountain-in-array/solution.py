class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        upper_len = 0
        res = 0
        lower_len = 0
        for idx, n in enumerate(arr):
            if idx == 0 or n > arr[idx-1]:
                upper_len += 1
                if lower_len > 0:
                    upper_len = 2
                lower_len = 0
            elif n == arr[idx-1]:
                upper_len = 1
                lower_len = 0
            else:
                lower_len += 1
                if upper_len >= 2:
                    res = max(res, lower_len+upper_len)
            print("idx", idx, "upper len", upper_len, "lower len", lower_len)
    
        return res
