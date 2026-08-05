class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        conns = {}
        ends = {}
        nodes = set([num for num in range(n)])
        all_nodes = list(nodes.copy())
        for start, end in invocations:
            conns.setdefault(start, []).append(end)
            
        explored = set([k])
        q = deque([k])
        nodes.remove(k)

        while q:
            cur = q.popleft()
            for conn in conns.get(cur, []):
                if conn not in explored:
                    explored.add(conn)
                    nodes.remove(conn)
                    q.append(conn)
        print("exp", explored, "nodes", nodes)
        for node in nodes:
            for conn in conns.get(node,[]):
                if conn in explored:
                    return all_nodes
        
        return list(nodes)
