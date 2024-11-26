class RangeModule(object):

    def __init__(self):
        self.intervals = []
        return
        
        
    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        if self.intervals == []:
            self.intervals = [(left, right)]
            return
        left_idx = 0 
        right_idx = len(self.intervals) 
        while left_idx < right_idx:
            
            med_idx = (right_idx+left_idx) // 2
            #print("intervals", self.intervals)
            #print("med", med_idx)
            #print("left", left_idx)
            #print("right", right_idx)

            if self.intervals[med_idx][0] <= left and self.intervals[med_idx][1] >= left and self.intervals[med_idx][1] >= right:
                return 
            elif self.intervals[med_idx][0] <= left and self.intervals[med_idx][1] >= left and self.intervals[med_idx][1] < right:
                
                self.intervals[med_idx] = (self.intervals[med_idx][0], right)
                
                try:
                    rest = self.intervals[med_idx+1:].copy()
                    for r in rest:
                        if right >= r[0]:
                            self.intervals.remove(r)
                            self.intervals[med_idx] = (self.intervals[med_idx][0], max(right, r[1]))
                except:
                    pass
                return 
            elif med_idx < len(self.intervals) - 1 and self.intervals[med_idx][1] < left and self.intervals[med_idx+1][0] > left:
                
                if self.intervals[med_idx+1][0] > right :
                    self.intervals.insert(med_idx+1, (left, right))
                else:
                    self.intervals[med_idx+1] = (left, max(self.intervals[med_idx+1][1], right))
                    try:
                        rest = self.intervals[med_idx+2:].copy()
                        for r in rest:
                            if right >= r[0]:
                                self.intervals.remove(r)
                                self.intervals[med_idx+1] = (self.intervals[med_idx+1][0], max(right, r[1]))
                    except:
                        pass
            
            elif self.intervals[med_idx][0] > left:
                right_idx = med_idx
            elif self.intervals[med_idx][1] < left:
                left_idx = med_idx+1
            right_idx = min(right_idx, len(self.intervals))
            #print("right", right_idx)
            #print("left", left_idx)
        if right_idx == 0:
            self.intervals.insert(0, (left, right))
            rest = self.intervals.copy()
            for r in rest[1:]:
                if right >= r[0]:
                    #print("intervals", self.intervals)
                    #print("r", r)
                    self.intervals.remove(r)
                    if right <= r[1]:
                        self.intervals[0] = (left, r[1])
                        break

        if left_idx == len(self.intervals):
            self.intervals.append((left, right))

        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        if not self.intervals:
            return False
        
        left_idx = 0 
        right_idx = len(self.intervals) 
        while left_idx < right_idx:
            med_idx = (right_idx+left_idx) // 2
            #print("left", left_idx)
            #print("right", right_idx)
            #print("med idx", med_idx)
            #print("med", self.intervals[med_idx])
            if self.intervals[med_idx][0] <= left and self.intervals[med_idx][1] >= left and self.intervals[med_idx][1] >= right:
                return True
            elif self.intervals[med_idx][0] <= left and self.intervals[med_idx][1] >= left and self.intervals[med_idx][1] < right:
                return False
            elif self.intervals[med_idx][0] > left:
                right_idx = med_idx
            elif self.intervals[med_idx][1] < left:
                left_idx = med_idx+1
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        if self.intervals == []:
            return 
        left_idx = 0 
        right_idx = len(self.intervals) 
        while left_idx < right_idx:

            med_idx = (right_idx+left_idx) // 2

            if self.intervals[med_idx][0] == left and self.intervals[med_idx][1] == right:
                del self.intervals[med_idx]
                return 
            elif self.intervals[med_idx][0] == left and self.intervals[med_idx][1] > right:
                self.intervals[med_idx] = (right, self.intervals[med_idx][1])
                return 
            elif self.intervals[med_idx][0] < left and self.intervals[med_idx][1] == right:
                self.intervals[med_idx] = (self.intervals[med_idx][0], left)
                return
                
            elif self.intervals[med_idx][0] < left and self.intervals[med_idx][1] > right:
                prev_left = self.intervals[med_idx][0]
                self.intervals[med_idx] = ( right, self.intervals[med_idx][1])
                self.intervals.insert(med_idx, (prev_left, left))
                return 
                
            elif self.intervals[med_idx][0] <= left and self.intervals[med_idx][1] > left and self.intervals[med_idx][1] < right:
                if self.intervals[med_idx][0] == left:
                    del self.intervals[med_idx]
                    med_idx -= 1
                else:
                    self.intervals[med_idx] = (self.intervals[med_idx][0], left)
                try:
                    
                    rest = self.intervals[med_idx+1:].copy()
                    
                    for r_idx, r in enumerate(rest):
                        print("r", r)
                        print("right", right)
                        if right >= r[1]:
                            self.intervals.remove(r)
                        else:
                            if right >= r[0]:
                                self.intervals[med_idx+1] = (right, r[1])
                            break
                except:
                    pass
                return 

            elif self.intervals[med_idx][0] > left:
                right_idx = med_idx
            elif self.intervals[med_idx][1] <= left:
                left_idx = med_idx+1


        if right_idx == 0:
            rest = self.intervals.copy()
            last_idx = -1
            num_removed = 0 
            for idx, r in enumerate(rest):
                if right >= r[0]:
                    if r[1] > right:
                        self.intervals[idx - num_removed] = (right, r[1])
                    else:
                        self.intervals.remove(r)
                        num_removed += 1
        elif right > self.intervals[med_idx][0] and left < self.intervals[med_idx][1]:
            self.removeRange(self.intervals[med_idx][0], right)       
        elif med_idx < len(self.intervals)-1 and right > self.intervals[med_idx+1][0] and left < self.intervals[med_idx+1][1]:
            self.removeRange(self.intervals[med_idx+1][0], right)

            


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
