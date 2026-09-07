class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        nums = nums + [float('inf')]
        res = 0
        rem = k
        def get_sum(start, end):
            end_sum = end * (end+1) / 2
            start_sum = (start-1) * start / 2
            return end_sum - start_sum 
        for idx, n in enumerate(nums):
            if idx == 0:
                cur_start = 1
            else:
                cur_start =  nums[idx-1] + 1
            cur_end = min(cur_start + rem - 1, n-1)
            rem -= cur_end - cur_start + 1
            res += get_sum(cur_start, cur_end)
            if rem == 0:
                return int(res)
        cur_start = nums[-1] + 1
        cur_end = cur_start + rem - 1
        res += get_sum(cur_start, cur_start)
        return int(res)
            

