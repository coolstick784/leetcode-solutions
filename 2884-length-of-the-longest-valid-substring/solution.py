from collections import deque
import heapq
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        matches = []

        tree = {}
        for f in forbidden:
            cur = tree
            for idx, ch in enumerate(f):
                cur.setdefault(ch, {})

                cur = cur[ch]
                if idx == len(f) - 1:
                    cur[True] = len(f)
        
        trees = [tree]
        #print("f", f, "trees", trees)
        for idx, ch in enumerate(word):
            new_trees = []
            for t in trees:
                if ch in t:
                    cur = t[ch]
                    if True in cur:
                        
                        matches.append((idx - cur[True] +1, idx)) 
                    else:
                        new_trees.append(cur)

            new_trees.append(tree)
            trees = new_trees.copy()
        #print(matches)

        heap = []
        for b, e in matches:
            heapq.heappush(heap, (e, b))

        res = 0
        mx_end = {}
        for idx in range(len(word)):
            mx_end[idx] = len(word) - 1
        for idx, ch in enumerate(word):
            while heap and heap[0][1] < idx:
                heapq.heappop(heap)
            if heap:
                mx_end[idx] = min(mx_end[idx], heap[0][0]-1)




        #print(mx_end)
        return max([mx_end[idx] - idx + 1 for idx in mx_end])


