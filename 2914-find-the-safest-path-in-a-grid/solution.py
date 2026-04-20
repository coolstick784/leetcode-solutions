# first, score all cells with their closeness score
# then, use sdkistra's algo to ask the question: for each cell we can go to, what's our score if our path ends at that cell?
# then, just keep going to the lowest score
# once we reach the end, return our score

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        scores = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dq = deque([])

        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 1:
                    scores[r][c] = 0
                    dq.append((r, c))

        while dq:
            r, c = dq.popleft()

            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and scores[nr][nc] is None:
                    scores[nr][nc] = scores[r][c] + 1
                    dq.append((nr, nc))
        def push_to_heap(r, c, cur_score):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            new_score = min(cur_score, scores[r][c])
            if new_score > best[r][c]:
                heapq.heappush(heap, (-new_score, r, c))

        heap = [(-1*scores[0][0], 0 , 0)]
        best = [[-1*float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        while heap:
            score, r, c = heapq.heappop(heap)
            score = -1 * score
            
            if score <= best[r][c]:
                continue
            if r == len(grid) -1 and c == len(grid[0]) - 1:
                return score
            best[r][c] = score
            push_to_heap(r+1, c, score)
            push_to_heap(r-1, c, score)
            push_to_heap(r, c+1, score)
            push_to_heap(r, c-1, score)



