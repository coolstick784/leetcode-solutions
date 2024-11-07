class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        self.nums.insert(self.insertVal(val, self.nums), val)
        #print("new", self.nums)
        return self.nums[-self.k]
    def insertVal(self,val, nums, idx = 0):
        #print("val", val)
        #print("nums", nums)
        
        med_idx = len(nums) // 2
        #print("med idx", med_idx)
        if nums == [] or val <= nums[0]:
            #print("return1")
            return idx
        if val >= nums[-1]:
            #print("return2")
            return idx + len(nums)
        if val >= nums[0] and val <= nums[1]:
            #print("return3")
            #print(idx+1)
            return idx+1
        if val == nums[med_idx]:
            #print("return")
            return idx + med_idx
        if val > nums[med_idx]:
            return self.insertVal(val, nums[med_idx:], idx+med_idx)
        elif val < nums[med_idx]:
            return self.insertVal(val, nums[:med_idx], idx)



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
