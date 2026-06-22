# first, ask if it's over 99 minutes and 60 seconds
# if so, move there
# then, move to the minute
# then, move to the seconds

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60
        numbers = [0, 0, 0, 0]
        if minutes >= 99:
            minutes = 99
            seconds = targetSeconds - 99 * 60
        numbers[1] = minutes % 10
        minutes = minutes // 10
        numbers[0] = minutes
        numbers[3] = seconds % 10
        seconds = seconds // 10
        numbers[2] = seconds
        

        numbers2 = numbers.copy()
        if numbers[2] * 10 + numbers[3] <= 39:
            minutes = numbers[0] * 10 + numbers[1]
            minutes -= 1
            numbers2[1] = minutes % 10
            minutes = minutes // 10
            numbers2[0] = minutes
            seconds = numbers[2] * 10 + numbers[3] + 60
            numbers2[3] = seconds % 10
            seconds = seconds // 10
            numbers2[2] = seconds

        def solve(p, startAt):
            res = 0

            for idx, n in enumerate(p):
                if idx == 0 and n == 0:
                    continue
                if idx == 1 and n == 0 and numbers[0] == 0:
                    continue
                if idx == 2 and n == 0 and numbers[0] == 0 and numbers[1] == 0:
                    continue
                if n != startAt:
                    res += moveCost
                res += pushCost
                startAt = n
            return res
        
        return min(solve(numbers, startAt), solve(numbers2, startAt))
