class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diffs = set()
        for idx, n in enumerate(arr):
            if idx == 0:
                continue
            diffs.add(n-arr[idx-1])
        if len(diffs) == 1:
            return True
        return False
        
