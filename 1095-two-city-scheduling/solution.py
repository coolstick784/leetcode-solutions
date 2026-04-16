# find the indices with the highest differences in cost
# then, for those, put them in their min city
# once one city is filled, calculate

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for idx, c in enumerate(costs):
            a = c[0]
            b = c[1] 
            diff = abs(a-b)
            heapq.heappush(diffs, (-1*diff, idx))
        a = set()
        b = set()
        #print("heap", diffs)
        while (len(a) + len(b)) < len(costs):
            cur, idx = heapq.heappop(diffs)
            if costs[idx][0] < costs[idx][1] and len(a) < len(costs)/2:
                a.add(idx)
            else:
                if len(b) < len(costs)/2:
                    b.add(idx)
                else:
                    a.add(idx)
        res = 0
        #print("a", a, "b", b)
        for idx in a:
            res += costs[idx][0]
        for idx in b:
            res += costs[idx][1]
        return res
        
