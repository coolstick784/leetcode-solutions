class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        # have a dictionary with edges, and we'll start from 0, then keep expanding out until there's no more to expand
        # so basically, e.g. 0 converts to 1 with factor 3, and 2 with factor 6, 
        # so the unit at 1 is 3 and 2 is 6
        # then, say 1 goes to 4 with factor 4, then 4 is 3 * 4 = 12, so we'll pass in the previous value
        # make it a q, with the new number, and the previous factor

        # {0: [(1, 2)], 1:[(2, 3)]}
        # [(1, 2)]

        edges = {}
        for start, end, factor in conversions:
            edges.setdefault(start, []).append((end, factor))
        res = [None for _ in range(len(conversions)+1)]
        
        q = deque([(0, 1)])
        while q:
            n, factor = q.popleft()
            res[n] = factor
            for edge, multiplier in edges.get(n, []):
                q.append((edge, (factor * multiplier) % (10**9+7)))
        return res 

