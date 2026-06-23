import bisect
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        mx = max(arr)
        after = sum(arr)
        before = 0
        idx = 0
        res = float('inf')
        out = None
        for n in range(0, mx + 1):
            
            while idx < len(arr) and n >= arr[idx]:
                before += arr[idx]
                idx += 1
            num_after = len(arr) - idx


                
            sol = abs(target - (before + num_after * n))

            if sol < res:
                out = n
                res = sol
            
            
        return out 
