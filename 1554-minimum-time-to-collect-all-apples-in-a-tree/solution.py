class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)
        
        def solve(cur):
            res = 0
            for conn in conns.get(cur, set()):
                conns[conn].remove(cur)
                res += 2 + solve(conn)
            if res == 0 and not hasApple[cur]:

                return -2
            if cur in conns:
                del conns[cur]
            return res

        
        return max(0, solve(0))
