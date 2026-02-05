import heapq
from typing import List

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []   # store negative distances; heap[0] is most negative = largest distance among kept k
        res = []

        for x, y in queries:
            d = abs(x) + abs(y)

            if len(heap) < k:
                heapq.heappush(heap, -d)
                res.append(-heap[0] if len(heap) == k else -1)
            else:
                # current kth-smallest distance is -heap[0]
                kth = -heap[0]

                # if d is not smaller than kth, answer doesn't change
                if d >= kth:
                    res.append(kth)
                else:
                    # replace the current largest among the k kept distances
                    heapq.heapreplace(heap, -d)  # pop+push in one step
                    res.append(-heap[0])

        return res

