# which friendships cant communicate?
# of those, which ones dont speak the language we are trying to instill

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        res = float('inf')
        languages = [set(l) for l in languages]
        conns = set()
        language_needs = {}
        for u, v in friendships:
            if not languages[u-1].intersection(languages[v-1]):
                conns.add((u, v))
        
        for l in range(1, n+1):
            explored = set()
            for u, v in conns:
                if l not in languages[u-1]:
                    explored.add(u)
                if l not in languages[v-1]:
                    explored.add(v)
           
            res = min(res, len(explored))
        return res

        

