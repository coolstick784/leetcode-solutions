# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we have a dict of distances
# each distnace will be a heap, with (-total height, val)
#we will also have mp that maps node values to distances
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
  
        distances = {}
        mp = {}
        def dfs(node, dist):
            if not node:
                return 0
            distances.setdefault(dist, [])
            mp[node.val] = dist
            mx = 1
            mx = max(mx, 1 + dfs(node.left, dist + 1))
            mx = max(mx, 1 + dfs(node.right, dist + 1))
            heapq.heappush(distances[dist], (-mx, node.val))
            return mx


        dfs(root, 0)
        res = []
        for q in queries:
            dist = mp[q]
            cur_dist = distances[dist]
            pre = None
            if cur_dist[0][1] == q:
                pre = heapq.heappop(cur_dist)
            if not cur_dist:
                res.append(dist-1)
            else:
                res.append(-1*cur_dist[0][0]+dist-1)
            if pre:
                heapq.heappush(distances[dist], pre)

        return res
