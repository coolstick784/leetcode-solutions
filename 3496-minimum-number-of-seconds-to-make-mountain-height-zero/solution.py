# we want to know how many seconds we have to wait until we can access a worker, and then after we wait, how many seconds the worker will take
# (number of seconds total to get the job done one more time, seconds to wait, seconds it will take, original time)



# (1, 0, 1, 1)
# (3, 1, 2, 1)
# (6, 3, 3, 1)

# (next_time + (time_to_job+og_time)  , next_time, time_to_job + og_time, og_time)
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        for t in workerTimes:
            heapq.heappush(heap, (t, 0, t, t))
        cur = 0
        res = 0
        while cur < mountainHeight:
            next_time, wait_time, time_to_job, og_time = heapq.heappop(heap)
            res = max(res, next_time)
            heapq.heappush(heap, (next_time + og_time + time_to_job,next_time, time_to_job+og_time, og_time))
            cur += 1
        return res
