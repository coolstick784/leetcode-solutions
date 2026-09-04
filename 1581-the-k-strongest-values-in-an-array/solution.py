class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        s = sorted(arr)
        c = s[(len(arr)-1) // 2]
        arr = [(abs(n-c), n) for n in arr]
        arr.sort()
        print(arr)
        return [v for d, v in arr[-k:]]
       
