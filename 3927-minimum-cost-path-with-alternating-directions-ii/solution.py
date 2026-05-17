class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        heap = [(1, 0, 0, 1)] # cost, row, col, seconds
        best = {(0, 0, 1): 1}

        def explore(row, col, next_row, next_col, prev_cost, prev_seconds):
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                return 

            cost = prev_cost

            # wait on CURRENT cell, not next cell
            if prev_seconds % 2 == 0:
                cost += waitCost[row][col]
                prev_seconds += 1

            # then move into next cell
            cost += (next_row + 1) * (next_col + 1)

            if cost >= best.get((next_row, next_col, (prev_seconds + 1) % 2), float('inf')):
                return

            best[(next_row, next_col, (prev_seconds + 1) % 2)] = cost
            heapq.heappush(heap, (cost, next_row, next_col, prev_seconds + 1))

        while heap:
            cost, row, col, seconds = heapq.heappop(heap)

            if row == m - 1 and col == n - 1:
                return cost

            explore(row, col, row + 1, col, cost, seconds)
            explore(row, col, row, col + 1, cost, seconds)
