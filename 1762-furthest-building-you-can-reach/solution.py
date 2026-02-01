class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # At the end point, it's optimal to use L ladders on the L highest differences
        # We need to find the end point, and also the L highest differences. 
        # To check if a building is the end point, we subtract the sum of the L highest differences from the running total
        # If the total differences is > bricks, then move back a step. Otherwise, keep going

        heap = []
        len_heap = 0
        cur_bricks = bricks
        lth_highest = 0
        for idx, h in enumerate(heights[:-1]):
            cur_diff = max(0, heights[idx+1] - h)

            if cur_diff > lth_highest and ladders > 0:
                heapq.heappush(heap, cur_diff)
                len_heap += 1
                if len_heap > ladders:
                    drop = heapq.heappop(heap)
                    cur_bricks -= drop
                    len_heap -= 1
                if len_heap == ladders:
                    lth_highest = heap[0]
            else:
                cur_bricks-= cur_diff

            if cur_bricks  < 0:
                return idx
            

            
        return len(heights) - 1
