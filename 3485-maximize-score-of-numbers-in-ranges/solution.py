class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        mx = max(start)+d
        left = 0



        def possible(n):
            prev = -float('inf')

            for idx, p in enumerate(start):
                if p - prev >= n:
                    prev = p
                else:
                    right = p + d
                    if right < prev + n:
                
                        return False
                    prev = prev + n
 
            return True
                
        while left < mx:
            med = (left + mx) // 2 + 1
            if not possible(med):
                mx = med - 1
            else:
                left = med
        return left 
