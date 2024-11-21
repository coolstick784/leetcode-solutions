import random
class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.n_poss = n - len(blacklist)
        self.n = n
        blacklist.sort()
        self.blacklist = blacklist
        self.add = {0:0}
        cur_add = 0 
        b_idx = 0 
        if blacklist:
            cur_in = blacklist[b_idx]
            while cur_in < self.n_poss:
                #print("cur in", cur_in)
                #print("cur add", cur_add)
                
                if b_idx <= len(blacklist) - 1 and (cur_in+cur_add) >= blacklist[b_idx]:
                    add_num = self.findLen(blacklist, b_idx)
                    cur_add += add_num
                    self.add[cur_in] = cur_add
                    #print("add num", add_num)
                    b_idx += add_num
                if b_idx >= len(blacklist):
                    break
                if (cur_in + cur_add) < blacklist[b_idx]:
                    cur_in = blacklist[b_idx] - cur_add
                else:
                    cur_in += 1
            
                
                
        self.keys = list(self.add.keys())        
            
        #print(self.add)

    def findLen(self, blacklist, start_idx):
        in_a_row = 1
        if start_idx > len(blacklist) - 1:
            return 0
        cur_idx = start_idx
        while cur_idx < (len(blacklist) -1) and blacklist[cur_idx+1] == blacklist[cur_idx] + 1:
            in_a_row += 1
            cur_idx += 1
        return in_a_row
    def findNearest(self, og, keys):
        #print("keys", keys)
        med = len(keys) // 2
        if len(keys) == 0 or og < keys[0]:
            return 0
        if og > keys[-1]:
            return self.add[keys[-1]]


        if og > keys[med]:
            return self.findNearest(og, keys[med:])
        if og == keys[med]:
            return self.add[keys[med]]
        if og < keys[med]:
            return self.findNearest(og, keys[:med])

    def pick(self):
        """
        :rtype: int
        """

        og = int(random.random() * self.n_poss)
        new = og + self.findNearest(og, self.keys)
        #print("og", og)
        #print("new", new)
        return new
