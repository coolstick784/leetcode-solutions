class Solution(object):
    def insertIntoBST(self, root, val):
        self.sorted_list = [-1e999]
        self.getSorted(root)
        self.sorted_list.append(1e999)
        self.sorted_idx = 0
        self.done = False
        self.root = root
        self.root = self.insertVal(self.root, val)
        
        return self.root
        
    def getSorted(self, node):
        if not node:

            return
        self.getSorted(node.left)
        self.sorted_list.append(node.val)
        self.getSorted(node.right)
    def insertVal(self, node, val):
        if not node:
            
            if val > self.sorted_list[self.sorted_idx] and val < self.sorted_list[self.sorted_idx + 1] and not self.done:
                
                node = TreeNode(val)
                self.done = True
                #print(self.sorted_list[self.sorted_idx])
            return node
        

        node.left = self.insertVal(node.left, val)
        self.sorted_idx += 1
        #print("idx", self.sorted_idx)
        #print("sorted val", self.sorted_list[self.sorted_idx])
        #print("actual val", node.val)
        node.right = self.insertVal(node.right, val)
        return node
