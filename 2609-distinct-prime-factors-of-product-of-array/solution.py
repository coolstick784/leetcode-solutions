class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # For each number 2 - 1000, list the prime numbers it is divisible by, and then just add that element in the array
        arr = [set() for n in range(2, 1001)]
        arr.insert(0, set())
        arr.insert(0, set())
        for n in range(2, 1001):
            if arr[n] == set():
                cur = n
                while cur < 1001:
                    
                    arr[cur].add(n)
                    cur += n
        res = set()
        for n in nums:
            res = res.union(arr[n])
        print("res", res)
        return len(res)
        
