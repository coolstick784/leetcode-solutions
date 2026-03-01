class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        ctr = {}
        uniq = 0

 
        din = "right"
        
        # if there are too many, move the left over 
        # if there are the exact amount or too little, move the right over

        # we want to know that there are n distinct integers, and that if we extend mul units over, there will still be n distinct integers. that is our mul
        # find the smallest subarrays, and then the largest subarrays, and add their differences to the total
        # the smallest and largest subarrays should end at the same number
        ends = {}
        past_equal = False

        while left < len(nums) and right < len(nums):
            if din == "right":
                cur = nums[right]
                if ctr.get(cur, 0) == 0:
                    ctr[cur] = 1
                    uniq += 1
                    #print("cur", cur)
                    #print("uniq", uniq)
                else:
                    ctr[cur] += 1
      
            else:
                cur = nums[left-1]
                if ctr[cur] == 1:
                    uniq -= 1
                    ctr[cur] = 0
                    
                   
                else:
                    ctr[cur] -= 1


            
            if uniq <= k:
                if uniq == k:
                    ends[right] = left
                din = "right"
                right += 1
            else:


                din = "left"
                left += 1


        left = 0
  
        right = 0
  

        ctr = {}
        uniq = 0
        res = 0

        rights = set(ends.keys())
        past_equal= False
        print("ends", ends)
        

        while left < len(nums) and right < len(nums):
            if din == "right":
                cur = nums[right]
                if ctr.get(cur, 0) == 0:
                    ctr[cur] = 1
                    uniq += 1
                    #print("cur", cur)
                    #print("uniq", uniq)
                else:
                    ctr[cur] += 1
      
            else:
                cur = nums[left-1]
                if ctr[cur] == 1:
                    uniq -= 1
                    ctr[cur] = 0
                    
                   
                else:
                    ctr[cur] -= 1


            
            if uniq < k:
                if past_equal:
                    print("left", left-1)
                    print("ends", ends[right])

                    res += (left-1) - ends[right] + 1
                din = "right"
                right += 1
            else:


                din = "left"
                left += 1
                if uniq == k:

                    past_equal = True
                else:
                    past_equal = False
        if past_equal and left == len(nums):
            res += left - ends[len(nums) - 1] 
        

        return res




