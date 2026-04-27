# do binary search and manually calculate the hours for each 
# keep moving until our left is <= the hour and the right is > the hour
# if the middle is >, move the right to the middle
# if it's <, move the left to the middle
# if it's equal, return the middle
# if left == right - 1, return left
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10 ** 7 + 1

        
        if len(dist)-1 >= hour:
            return -1
        def calculateHour(n):
            if n == 0:
                return float('inf')
            out = 0
            for d in dist[:-1]:
                out += math.ceil(d/n)
            out += float(dist[-1])/float(n)
            return out 
        while True:
            mid = (left + right) // 2
            cur = calculateHour(mid)

            if cur == hour:
                return mid
            if cur < hour and calculateHour(mid-1) > hour:
                return mid
            if cur < hour:
                right = mid
            elif cur > hour:
                left = mid



