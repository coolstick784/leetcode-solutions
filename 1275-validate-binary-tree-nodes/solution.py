# the root has no parent -- by default checked
# each parent has at most 2 children -- by default checked
# each non root node has 1 parent
# a node cannot be its own parent

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {}
        children = {}
        for node in range(n):
            parent[node] = None
        
        roots = 0
        root = None

        for idx, l in enumerate(leftChild):
            r = rightChild[idx]
            if l == idx or r == idx:
                return False
            
            if (r != -1 and parent[r] is not None) or (l != -1 and parent[l] is not None):
                return False
            if parent[idx] == r or parent[idx] == l:
                return False
            parent[r] = idx
            parent[l] = idx
            if r != -1:
                children.setdefault(idx, []).append(r)
            if l != -1:
                children.setdefault(idx, []).append(l)

        
        explored = set()
        for node in range(n):
           
            if parent[node] is None:
                roots += 1
                if roots >= 2:
                    return False
                root = node

        def explore(node):
            if node in explored:
                return 
            explored.add(node)
            for child in children.get(node, []):
                explore(child)
            

        explore(root)
        if len(explored) != n:
            return False
   
        if roots == 0:
            return False
        return True
