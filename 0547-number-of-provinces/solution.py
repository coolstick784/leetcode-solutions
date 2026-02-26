class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        conn_dict = {}
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):

                if isConnected[r][c] == 1:
                    conn_dict.setdefault(r, []).append(c)
        print("conn dict", conn_dict)
                    
        
        q = deque([])
        for r in conn_dict:
            if conn_dict[r] != []:
        
                q.append(r)
                while q:
     
                    cur = q.popleft()
                    for c in conn_dict[cur]:
                        q.append(c)
                    conn_dict[cur] = []
                res += 1
                
                    
                        
        return res
                    
