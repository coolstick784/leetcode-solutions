# for each left index, if we start at that index, what's the highest we can do?
# if start idx > 0 and all ascending, return length + 1 -- length = right - left + 1
# we can either accept one break, and compare all future elements to prev, or start at the break

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        @lru_cache(None)
        def solve(start_idx):

            left = start_idx
            right = start_idx
            prev = nums[left]
            brk = False
            compare = 1
            while left < len(nums) and right < len(nums)-1:
              
                if nums[right+1] >= prev:
                    prev = nums[right+1]
                    right += 1
                elif brk:
                    break
                else:
                    brk = True
                    back = nums[max(start_idx, right-1)]
                    if back <= nums[right+1]:
                        prev = min(nums[right+1], nums[right])
                    
                    compare = solve(right+1)
                    right += 1

                
            

            
            out = right - left + 1
            if start_idx > 0 and not brk:
                out += 1
          
            return max(out, compare)
            

                
                
        
        return solve(0)
        
