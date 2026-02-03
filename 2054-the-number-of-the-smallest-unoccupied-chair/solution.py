import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        # Sort friends by arrival time
        arrivals = sorted((start, leave, i) for i, (start, leave) in enumerate(times))

        free = list(range(n))      # available chair numbers
        heapq.heapify(free)

        occupied = []              # (leave_time, chair)

        for start, leave, i in arrivals:
            # Free chairs for anyone who already left
            while occupied and occupied[0][0] <= start:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free, chair)

            chair = heapq.heappop(free)
            heapq.heappush(occupied, (leave, chair))

            if i == targetFriend:
                return chair

        return -1

