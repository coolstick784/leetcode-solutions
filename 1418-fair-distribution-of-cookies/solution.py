class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        avg = sum(cookies) / k
        def minMax(scores, idx):
            if idx == len(cookies):
                return max(scores)
            c = cookies[idx]
            out = float('inf')
            
            explored = set()
            for child in range(k):
                if scores[child] > avg:
                    continue
                if scores[child] in explored:
                    continue
                explored.add(scores[child])
                cur = scores.copy()
                cur[child] += c
                out = min(out, minMax(cur, idx+1))
            
            return out

        return minMax([0 for _ in range(k)], 0)
