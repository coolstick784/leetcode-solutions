class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        num_odd = [0 for _ in arr]
        num_even = [0 for _ in arr]
        new = []
        for n in arr:
            if n % 2:
                new.append(False)
            else:
                new.append(True)
        res = 0
        cur_odd = 0
        cur_even = 0
        for idx in range(len(arr)-1, -1, -1):
            cur = new[idx]
            if cur:
                cur_even += 1
            else:
                cur_odd += 1
            if idx == len(arr) - 1:
                num_odd[idx] = cur_odd
                num_even[idx] = cur_even
            elif cur:
                num_odd[idx] = num_odd[idx+1]
                num_even[idx] = 1 + num_even[idx+1]
            else:
                num_odd[idx] = 1 + num_even[idx+1]
                num_even[idx] = num_odd[idx+1]
            res += num_odd[idx]
            res = res % (10**9+7)
        return res
