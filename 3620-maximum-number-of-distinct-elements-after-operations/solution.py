#First, sort the list
# Then, starting with the lowest number, add it to the lowest possible n in the range
# For each number after that, get the difference between that and the new number before it
# If the difference is > k, subtract the lowest
# If it's < k and < (-k), make it so that the new number is 1 + the previous number
# Otherwise, if it's -k, move on and set that current number to the previous number
# For example, in [4, 4, 4, 4], we'd set the first one to 3, 2nd to 5, since the 3rd is still 4, current will still be 5
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for idx, n in enumerate(nums):
            if idx == 0:
                cur_num = n - k
                res += 1
            else:
                diff = n - cur_num
                if diff > k:
                    cur_num = n - k
                    res += 1
                elif diff <= k and diff > (-1*k):
                    cur_num = n - diff + 1
                    res += 1
                else:
                    continue


        return res

        
