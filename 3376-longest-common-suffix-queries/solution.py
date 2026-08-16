import heapq
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tree = {}
        for idx, w in enumerate(wordsContainer):
            cur = tree
            cur.setdefault("best", (float('inf'), float('inf')))
            if len(w) < cur['best'][0]:
                cur['best'] = (len(w), idx)
            
            for w_idx in range(len(w)-1, -1, -1):
                ch = w[w_idx]
                cur.setdefault(ch, {})
                cur = cur[ch]
                cur.setdefault("best", (float('inf'), float('inf')))
                if len(w) < cur['best'][0]:
                    cur['best'] = (len(w), idx)
        res = []
        print("tree", tree.get('b'))
        for w in wordsQuery:
            cur = tree
            w_idx = len(w) - 1
            ch = w[w_idx]
            while cur.get(ch) and w_idx >= 0:
                w_idx -= 1
                cur = cur[ch]
                if w_idx >= 0:
                    ch = w[w_idx]
            res.append(cur['best'][1])
        return res
            

                
