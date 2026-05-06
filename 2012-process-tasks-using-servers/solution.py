import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = []
        busy = []

        for idx, weight in enumerate(servers):
            heapq.heappush(free, (weight, idx))

        res = []
        time = 0

        for task_idx, task_time in enumerate(tasks):
            time = max(time, task_idx)

            # release every server that is free by this time
            while busy and busy[0][0] <= time:
                finish_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # if no server is free, jump to the next finish time
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)
            res.append(idx)

            heapq.heappush(busy, (time + task_time, weight, idx))

        return res
