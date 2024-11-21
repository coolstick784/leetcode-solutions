
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ctr = 0 
        
        start = 0
        past_end = -1
        past_prod = -1
        self.i = 0 
        while start < len(nums):
            if past_end > start:
                cur_prod = past_prod
                end = past_end
            else:
                cur_prod = 1
                end = start
            
            while end < len(nums):
                #self.i+=1
                #print(self.i)
                cur_prod *= nums[end]
                #print("start", nums[start])
                #print("cur prod", cur_prod)

                if cur_prod >= k:
                    cur_prod = cur_prod / nums[end]
                    break
                end += 1
            
            past_end = max(start, end)
            past_prod = cur_prod / nums[start]
            
            #print("end", past_end)
            ctr += past_end - start
            #print("ctr", ctr)

            start += 1
                
        return ctr
        


