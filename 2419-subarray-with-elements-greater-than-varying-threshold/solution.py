#UNION find startign at the left
# starts will be leftmost
# first look right, and then set right union to cur
# then look left, then set cur union to left

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        if min(nums) > threshold / len(nums):
            return len(nums)
        if max(nums) > threshold:
            return 1
        nums = [(n, idx) for idx, n in enumerate(nums)]
        nums.sort()
        start = {}
        lengths = {}
        for idx in range(len(nums)):
            start[idx] = idx
       
        
        cur_idx = len(nums) - 1


        def trace(idx):
            if start[idx] == idx:
                return idx
            out = trace(start[idx])
            start[idx] = out
            return out
        def union(left, right):
            #print("left", left, "right", right, "lengths", lengths)
            left_start = trace(left)
            right_sol = lengths[right]
            start[right] = left_start
            lengths[left_start] = lengths[left_start] + right_sol
        explored = set()
        mx_len = 0
        for divisor in range(1, len(nums)):
            cur = threshold / divisor 
            while nums and nums[-1][0] > cur:
                n, idx = nums.pop()
                lengths[idx] = 1
                explored.add(idx)
                if idx + 1 in explored:
                    union(idx, idx+1)
                    
                if idx - 1 in explored:
                    union(idx-1, idx)
                mx_len = max(mx_len, lengths[trace(idx)])
                if mx_len >= divisor:
                    return divisor
                   
        return -1
        
        
