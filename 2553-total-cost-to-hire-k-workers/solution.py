import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = []
        right = []
        max_left = candidates-1
        min_right = len(costs) - candidates 
        for idx in range(candidates):
            heapq.heappush(left, (costs[idx], idx))
            heapq.heappush(right, (costs[len(costs) - idx - 1], len(costs)-idx-1))
        res = 0
        for w in range(k):
     
            if left:
                left_cost, left_idx = left[0]
            else:
                left_cost, left_idx = float('inf'), float('inf')
            if right:
                right_cost, right_idx = right[0]
            else:
                right_cost, right_idx = float('inf'), float('inf')
            if left_cost < right_cost or (left_cost == right_cost and left_idx < right_idx):
                res += left_cost
                heapq.heappop(left)
            elif right_cost < left_cost:
                res += right_cost
                heapq.heappop(right)
            else:
                res += left_cost
                heapq.heappop(left)
                heapq.heappop(right)
            if len(left) < candidates and candidates + w + 1 < len(costs):
                idx = max_left + 1
                
                if idx < min_right:
                    
                    heapq.heappush(left, (costs[idx], idx))
                    max_left = idx
            if len(right) < candidates and len(costs) - candidates - w - 1 >= 0:
                idx = min_right - 1
     
                if idx > max_left:
            
                    heapq.heappush(right, (costs[idx], idx))
                    min_right = idx

        return res

