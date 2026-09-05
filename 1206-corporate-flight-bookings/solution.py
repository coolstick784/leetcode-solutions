class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total = [0 for _ in range(n)]
        for start, end, seats in bookings:
            total[start-1] += seats
            if end < n:
                total[end] -= seats
        res = []
        cur = 0
        print(total)
        for n in total:
            cur += n
            res.append(cur)
        return res
