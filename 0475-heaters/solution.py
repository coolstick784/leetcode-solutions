class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        

        left = 0
        right = max(houses[-1], heaters[-1])
        def isPossible(cur):
            prev = 0
            cHouses = deque(houses)
   
            for h in heaters:
                while cHouses and cHouses[0] >= h - cur and cHouses[0] <= h + cur:
                    cHouses.popleft()
                if cHouses and cHouses[0] < h - cur:
                    return False
                if not cHouses:
                    return True
            return not cHouses
        while left < right:
            med = (left + right) // 2
 
            if isPossible(med):
                right = med
            else:
                left = med + 1

        return left

