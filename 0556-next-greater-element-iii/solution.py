# find the rightmost digit such that it's greater than the next digit, and swap them


# 223 
# 232
# if it's < the maximum, keep popping the max until it's <=

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        digits = [int(d) for d in digits]
        found = False
        heap = []
        for idx in range(len(digits)-1, -1, -1):
            cur = digits[idx]
            if heap and cur < -heap[0][0]:
                while heap and -heap[0][0] > cur:
                    prev_idx = heapq.heappop(heap)[1]

                digits[idx], digits[prev_idx] = digits[prev_idx], digits[idx]
                found = True
                break
            heapq.heappush(heap, (-cur, idx))
        if not found:
            return -1
        prev = digits[:idx+1]
        after = digits[idx+1:]
        after.sort()

        digits = prev + after
        p = 1
        res = 0
        for idx in range(len(digits)-1, -1, -1):
            res += p * digits[idx]
            p *= 10

        print(res)
        if res > 2**31-1:
            return -1
        

        return res
        
