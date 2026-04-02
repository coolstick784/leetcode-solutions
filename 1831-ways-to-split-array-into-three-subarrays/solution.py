# loop through each left subarry
# get the sum of all values up to that point
# for each left array, we want to find the minimum and maximum point of the right line such that mid >= left and right >= mid
# we can use binary search for this
# min point should be the 1st el in the middle arr
# max point should be the 1st el in the middle arr
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        sums = []
        cur_sum = 0
        res = 0
        def bisectArr(left_sum, left):
            min_point = max(bisect.bisect_left(sums, left_sum*2), left+1)

            if min_point >= len(sums):
                return [1, 0]
            diff = sums[-1] - sums[left]
          

            
            att = sums[left] + diff/2 + 0.01
         
            # we want to find the first point where the sum at that idx is greater than the average between the min point and end
            # then, subtract 1
            max_point = bisect.bisect_left(sums, att) - 1
            if max_point == len(sums) - 1 and att > sums[-1] + 0.01:
                return [1, 0]
            max_point = min(max_point, len(sums)-2)


            return [min_point, max_point]


        for n in nums:
            cur_sum += n
            sums.append(cur_sum)
        set_sums = set(sums)
   
        for left in range(len(nums)-2):

      
            left_sum = sums[left]
            min_point, max_point = bisectArr(left_sum, left)
          
            res += max(max_point - min_point+1, 0)
  

        return res % (10**9 + 7)
