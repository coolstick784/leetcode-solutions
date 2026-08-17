# create a tree based on all the patterns in rules
# we want the min cost for each idx/len combo
class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        ptree = {}
        dp = {}
        rtree = {}
        rs = {}
        for idx, (p, r) in enumerate(rules):
            cur = ptree
            cost = costs[idx] + p.count("*")
            cur_r = rtree
            
            for p_idx, ch in enumerate(p):
                cur.setdefault(ch, {})
                cur = cur[ch]
                if p_idx == len(p) - 1:
                    cur.setdefault(True, []).append((cost, len(p), idx))
            for r_idx, ch in enumerate(r):
                cur_r.setdefault(ch, {})
                cur_r = cur_r[ch]
                if r_idx == len(r) - 1:
                    cur_r.setdefault(True, []).append((len(r), idx))
        
        trees = []
        new_trees = []
        for idx, ch in enumerate(target):
            new_trees.append(rtree)
            trees = new_trees.copy()
            new_trees = []
            for tree in trees:
                if ch in tree:
                    if True in tree[ch]:
                        for l, r_idx in tree[ch][True]:
                      
                            start = idx - l + 1
                        
                            rs.setdefault(r_idx, set()).add(start)
                        
                    new_trees.append(tree[ch])
       
        
        
        trees = []
        new_trees = []
        if "*" in ptree:
            print("p", ptree["*"])
        for idx, ch in enumerate(source):
            new_trees.append(ptree)
            trees = new_trees.copy()
            new_trees = []
            dp[idx] = {}
            
            
            for tree in trees:
                
                
                if ch in tree:
                    
                    if True in tree[ch]:
                        for cost, l, m_idx in tree[ch][True]:
                        
                            
                            if idx-l+1 in rs.get(m_idx, set()) and cost < dp[idx-l+1].get(l, float('inf')):
                                dp[idx-l+1][l] = cost 
                    new_trees.append(tree[ch])
                if "*" in tree:
                
                    if True in tree["*"]:
                        for cost, l, m_idx in tree["*"][True]:

                            
                            if idx-l+1 in rs.get(m_idx, set()) and cost < dp[idx-l+1].get(l, float('inf')):
                                dp[idx-l+1][l] = cost 
                    
                    new_trees.append(tree["*"])
        
        print("dp", dp)
        print("rs", rs)
            
        @lru_cache(None)
        def solve(idx):
            if idx >= len(source):
                return 0
            out = float('inf')
            if source[idx] == target[idx]:
                out = min(out, solve(idx+1))
            for l in dp.get(idx):
                out = min(out, dp[idx][l] + solve(idx+l))
            return out

        res = solve(0)
        if res == float('inf'):
            return -1
        return res
