class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # 1. Sort the array using .sort()
        # 2. Get the number of set bits for each element and place them into a dictionary
        # 3. We want an intermediate list that has our current values
        # We want a left index that represents how many values we've currently moved
        # 4. In that intermediate list, move the first element in the sorted list to that position, based on the first index of the elemnent in the intermediate list
        # This should only check past what we've already moved
        # 5. If we can't swap an element, return False
        # 6. Continue the process until we've reached the end of the list


        sorted_arr = sorted(nums)
        set_bits = {}

        def getSetBits(num):
            max_bits = 9
            out = 0
            for b in range(max_bits+1):

                if (num >> b) & 1:
                    out += 1
            return out

        for n in nums:
            set_bits[n] = getSetBits(n)
        
        imd = nums.copy()
        left = 0
        
        while left < len(nums):
            cur_num = sorted_arr[left]
            cur_num_index = imd[left:].index(cur_num) + left
            idx = cur_num_index
            while idx != left:
                if set_bits[imd[idx-1]] == set_bits[cur_num]:
                    imd[idx-1], imd[idx] = imd[idx], imd[idx-1]
                else:
                    return False
                idx -= 1
            left += 1
        return True



