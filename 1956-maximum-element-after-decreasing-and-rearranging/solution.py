class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for idx, n in enumerate(arr):
            if idx == 0:
                arr[idx] = 1
                continue
            arr[idx] = min(n, arr[idx-1] + 1)
        return arr[-1]
