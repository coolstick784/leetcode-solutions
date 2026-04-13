class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        sorted_arr = sorted(arr)
        sorted_brr = sorted(brr)
        cost_k = k
        cost_no_k = 0

        for idx, el in enumerate(sorted_brr):
            cost_k  += abs(el - sorted_arr[idx])
        
        for idx, el in enumerate(brr):
            cost_no_k  += abs(el - arr[idx])
        return min(cost_k, cost_no_k)
