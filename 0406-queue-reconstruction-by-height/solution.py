import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        idxs = {}
        heap = []
        for h, k in people:
            if k > 0:
                idxs[(h, k, k)] = idxs.get((h, k, k), 0) + 1
            else:
                heapq.heappush(heap, (h, k))
        res = []
        while heap:
            nh, nk = heapq.heappop(heap)

            res.append((nh, nk))
            new = {}
            for h, k1, k2 in idxs:
                if h <= nh:
                    if k2 == 1:
                        heapq.heappush(heap, (h, k1))
                    else:
                        new[(h, k1, k2-1)] = idxs[(h, k1, k2)]
                else:
                    new[(h, k1, k2)] = idxs[(h, k1, k2)]
            idxs = new.copy()
        return res

