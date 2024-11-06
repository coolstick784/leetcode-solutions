class Solution(object):
    def findMode(self, root):
        self.modes = []
        self.count = 0
        self.cur_count = 0
        self.prev = -1e999
        self.loopThrough(root)
        return self.modes
    def loopThrough(self, node):
        
            
        if not node:
            return 
        
        self.loopThrough(node.left)
        #print("val", node.val)
        #print("prev", self.prev)
        #print("prev cur count", cur_count)
        
        if node.val == self.prev:
            self.cur_count += 1
            
        else:
            self.cur_count = 1

        self.prev = node.val
        if self.cur_count > self.count:
            self.modes = [node.val]
            self.count = self.cur_count
        elif self.cur_count == self.count:
            self.modes.append(node.val)
        
        self.loopThrough(node.right)

  
