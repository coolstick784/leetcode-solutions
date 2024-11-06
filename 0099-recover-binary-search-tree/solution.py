class Solution:
    def recoverTree(self, root):

        self.prev = -1e999
        self.min = -1e999
        self.max = -1
        self.last = -1e999
        self.getIncorrectMinMax(root)
        #print("og", self.root.val)
        #print("min", self.min)
        #print("max", self.max)
        self.replaceNode(root)


        #print("val", root.val)
    def replaceNode(self, node):
        if not node:
            return
        if node.val == self.min:
            node.val = self.max
            
            
        elif node.val == self.max:
            node.val = self.min
        self.replaceNode( node.left)
        self.replaceNode(node.right)
        
    def getIncorrectMinMax(self, node):
        if not node or node.val == 'NA' or node.val == None:
            return
        self.getIncorrectMinMax(node.left)
        #print(node.val)
        if self.prev >= node.val:
            if self.min == -1e999:
                self.min = self.prev
            self.max = node.val
        self.prev = node.val
        

        self.getIncorrectMinMax(node.right)

