class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([(start, 0)])
        explored = {start}

        while q:
            val, steps = q.popleft()

            for n in nums:
                for nxt in (val + n, val - n, val ^ n):
                    if nxt == goal:
                        return steps + 1

                    # only values from 0 to 1000 can keep being explored
                    if 0 <= nxt <= 1000 and nxt not in explored:
                        explored.add(nxt)
                        q.append((nxt, steps + 1))

        return -1
