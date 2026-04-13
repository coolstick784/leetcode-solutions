# a list of groups, and a list that we've explored
# create a dict/hashmap where we get the number of edges that are connected to that edge
# if we've already explored it, skip
# after we perform dfs and get the number of edges in that grouping, obviously add those edges to explored and keep going until there are no more edges to explore in our dfs
# then, get our current number in our group and multiply that by n - len(explored)

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        explored = set()
        starts = {}
        for start, end in edges:
            starts.setdefault(start, []).append(end)
            starts.setdefault(end, []).append(start)
        
        def dfs(cur):
            if cur in explored:
                return 0
            explored.add(cur)
            out = 1
            for end in starts.get(cur, []):
                out += dfs(end)
            return out 

        res = 0
        for edge in range(n):
            res += dfs(edge)  * (n - len(explored))
        return res
        
