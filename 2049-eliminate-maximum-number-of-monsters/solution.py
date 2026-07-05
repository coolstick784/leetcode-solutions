from collections import deque
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = []
        for idx, d in enumerate(dist):
            s = speed[idx]
            times.append(d/s)
        times.sort()
        times = deque(times)
        cur_t = 0
        
        while times:
            t = times.popleft()
            if t <= cur_t:
                return cur_t
            

            cur_t += 1
        return cur_t
