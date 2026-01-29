class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        len_arr = len(arr)
        if len_arr == 1:
            return 1
        left = 0
        if arr[0] == arr[1]:
            cur_max = 1
            dirn = "eq"
            left = 1
        elif arr[1] > arr[0]:
            dirn = "pos"
            cur_max = 2
        else:
            dirn = "neg"
            cur_max = 2
        
        
        for idx, n in enumerate(arr):
            if idx < 2:
                continue
            if arr[idx] > arr[idx-1] and dirn == "pos":
                left = idx-1
            elif arr[idx] < arr[idx-1] and dirn == "neg":
                left = idx-1 
            elif arr[idx] == arr[idx-1]:
                left = idx 
                dirn = "eq"
            elif arr[idx] > arr[idx-1] and dirn == "neg":
                dirn = "pos"
            elif arr[idx] < arr[idx-1] and dirn == "pos":
                dirn = "neg"
            elif arr[idx] > arr[idx-1] and dirn == "eq":
                dirn = "pos"
                left = idx - 1
            elif arr[idx] < arr[idx-1] and dirn == "eq":
                dirn = "neg"
                left = idx-1
            cur_max = max(cur_max, idx - left + 1)
        return cur_max
            


        
        
