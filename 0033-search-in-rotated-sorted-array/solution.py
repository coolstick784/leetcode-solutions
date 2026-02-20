class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        l = nums[left]
        r = nums[right]
        # looking for when l < r and l < nums[left-1]
        while l > r or l > nums[left-1]:
            l = nums[left]
            r = nums[right]
            med = (left + right) // 2

            m = nums[med]
            if m >= l :
                left = med + 1
            else:
                right = med
            l = nums[left]
            r = nums[right]
        low = left
        rightmost = nums[-1]
        # add len(nums) - low + 1
        #0 -> 4, 1-> 5, 2 -> 6, 3 -> 0, 4-> 1, 2-> 5, 6 -> 3

        l_nums = len(nums)
        # given what it should be, return what it is in the true array
        def normalize(idx,  low, right, l_nums):

            if idx <= l_nums - low - 1:
                return idx + low
            return idx - l_nums + low 
        left = 0
        right = len(nums) - 1
        while left < right:
            l = nums[normalize(left, low, rightmost, l_nums)]
            

            r = nums[normalize(right,  low, rightmost, l_nums)]
            if l > target or r < target:
                return -1
            med = (left + right) //2

           
        
            m = nums[normalize(med,  low, rightmost, l_nums)]

            
            if m < target:

                left = med + 1
            elif m > target:
                right = med
            else:
                return normalize(med,  low, rightmost, l_nums)
        if nums[normalize(left, low, rightmost, l_nums)] == target:
            return normalize(left, low, rightmost, l_nums)
        return -1

        
        


