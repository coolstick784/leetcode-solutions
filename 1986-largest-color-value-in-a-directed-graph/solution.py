class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.res = 0
        starts = {}
        ends = {}
        letters = [chr(ord('a') + ch) for ch in range(26)]
        conns = set()
        if not edges:
            return 1
        
        @lru_cache(None)
        def dfs(s):


   
            cur = {}
            for letter in letters:
                cur[letter] = 0
            cur[colors[s]] = 1
            for end in starts.get(s, set()):
                
                if (s, end) in conns:
        
                    return -1
                conns.add((s, end))
                new = dfs(end)
                if new == -1:
                    return -1

                for color in new:
                    add = 0
                    if color == colors[s]:
                        add = 1
                    cur[color] = max(cur[color], add + new[color])
            self.res = max(self.res, max(cur.values()))
           
            return cur
        for start, end in edges:
            starts.setdefault(start, set()).add(end)
            ends.setdefault(end, set()).add(start)
        found = False
        for start in starts:
            if start not in ends:
                val = dfs(start)
                if val == -1:
                    return -1
   
                found = True
        if not found:
            return -1
        return self.res 
