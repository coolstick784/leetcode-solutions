# most popular value on even and most popular value on odd, as well as econd most popular 
# if the most popular are differnet, it's the cost of even + cost of odd
# otherwise, it's the second most popular from odd with most popular on even or vice versa

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums) 
        if l % 2 == 0:
            num_even = l // 2
            num_odd = l //2
        else:
            num_even = l // 2 + 1
            num_odd = l // 2
        ctr_even = {}
        ctr_odd = {}
        for idx, n in enumerate(nums):
            if idx % 2 == 0:
                ctr_even[n] = ctr_even.get(n, 0) + 1
            else:
                ctr_odd[n] = ctr_odd.get(n, 0) + 1
        heap_even = []
        heap_odd = []
        for n in ctr_even:
            heapq.heappush(heap_even, (-ctr_even[n], n))
        for n in ctr_odd:
            heapq.heappush(heap_odd, (-ctr_odd[n], n))
        highest_even = []
        highest_odd = []
        highest_even.append(heapq.heappop(heap_even))
        if heap_even:
            highest_even.append(heapq.heappop(heap_even))
        else:
            highest_even.append((0, 0))
        for _ in range(2):
            if heap_odd:
                highest_odd.append(heapq.heappop(heap_odd))
            else:
                highest_odd.append((0, 0))
        
        def solve(even, odd):
            en = even[1]
            on = odd[1]
            if en == on:
                return float('inf')
            return (num_even + even[0]) + (num_odd + odd[0])

        
        res = float('inf')
        res = min([solve(highest_even[0], highest_odd[0]), solve(highest_even[0], highest_odd[1]), solve(highest_even[1], highest_odd[0])])
        return res
        
        
