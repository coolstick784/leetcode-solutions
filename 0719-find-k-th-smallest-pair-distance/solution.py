from collections import Counter
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ctr = 0 
        self.dict = dict(Counter(nums))
        self.dict = dict(sorted(self.dict.items()))
        
        keys = list(self.dict.keys())
        #print("dict", self.dict)
        
        nums = []
        values = []
        for idx, n in enumerate(keys):
            if idx > 0:
                nums.append(n-keys[idx-1])
                values.append(self.dict[n])
                
            else:
                nums.append(0)
                values.append(self.dict[n])

        self.nums = nums
        self.values = values
        self.jumps = [1 for _ in nums]
        self.sums = [0 for _ in nums]
        self.k = k


        def check_pairs(prev_X, prev_val, X):
            ctr = prev_val
            #print("jumps", self.jumps)
            #print("sums", self.sums)
            #print("nums", self.nums)
            jumps = self.jumps.copy()
            sums = self.sums.copy()
            if prev_X < 0:
                for idx, n in enumerate(self.nums):
                    ctr += self.values[idx] * (self.values[idx]-1)/2
            for idx, n in enumerate(self.nums):
                running_sum = self.sums[idx]
                try:
                    cur_jumps = self.jumps[idx]
                    for idx2, n2 in enumerate(self.nums[idx+cur_jumps:]):
                        running_sum += n2
                        #print("cur n", n)
                        #print("sum", running_sum)
                        #print("n2", n2)
                        if running_sum <= X:
                            ctr += self.values[idx] * self.values[idx+idx2+cur_jumps]
                            if ctr >= k:
                                return ctr

                        elif running_sum > X:
                            jumps[idx] += idx2 
                            sums[idx] = running_sum - n2
                            #print("breaking")
                            break
                        if (idx + idx2 + cur_jumps) == (len(self.nums)-1):
                            jumps[idx] = int(1e10)
                            sums[idx] = int(1e10)
                        
                    
                except Exception as e:
                    print(e)
                    pass
            #print("ctr", ctr)
            if ctr < k:
                self.jumps = jumps.copy()
                self.sums = sums.copy()
            return ctr

        diffs = {}
        ctr = 0 
        #print("nums", self.nums)
        '''        for X in range(0, int(1e7), 1000):
            ctr = check_pairs(X-1000, ctr, X)
            print("X", X)
            print("Ctr", ctr)
            if ctr >= k:
                return X'''
        left = 0 
        right = keys[-1] - keys[0]
        #print("zero")
        ctr = check_pairs(0-1000, ctr, 0)
        if ctr >= k:
            return 0
        prev_X = 0 
        while left < right:
            print("left", left)
            print("right", right)
            med = (left + right) // 2
            #print("med", med)
            next_ctr = check_pairs(prev_X, ctr, med)
            if next_ctr >= k:
                right = med
            elif next_ctr < k:
                ctr = next_ctr
                prev_X = med
                left = med+1
        return left
                
                
        
