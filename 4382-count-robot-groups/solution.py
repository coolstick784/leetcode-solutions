class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        res = len(position)
        robots = list(zip(position, speed))
        robots.sort()
        print(robots)
        for idx in range(len(robots)-2, -1, -1):
            p, s = robots[idx]
            next_s = robots[idx+1][1]
            next_p = robots[idx+1][0]
            if s > next_s or next_p - p <= distance:
                res -= 1
                robots[idx] = (p, next_s)
        
        return res
