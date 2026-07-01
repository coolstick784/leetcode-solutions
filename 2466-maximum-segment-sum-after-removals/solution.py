# 1. create a new list, new that has 0 at all remove query locations
# 2. calculate segment sums
# 3. starting from the end, we can combine segment sums and add the original number
# 4. for each query, we get the segment sum to the left, the segment sum to the right, and add both  
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        zeros = removeQueries
        new = nums.copy()
        for z in zeros:
            new[z] = 0
        pre = [0] #pre[idx] is before, pre[idx+1] is after
        for n in new:
            pre.append(n + pre[-1])
        sums = {idx: 0 for idx in zeros}
        mx = 0
        cur = 0
        for n in new:
            if n == 0:
                cur = 0
            else:
                cur += n
            mx = max(mx, cur)

        res = []

        union = {n:n for n in zeros}
        def merge(n1, n2):
            

            t2 = trace(n2)
            
            t1 = trace(n1)
            
            union[t1] = n1
            union[t2] = n1
            union[n1] = n1
            return 


        def trace(n):
    
            if n == -1:
                return -1
            if union.get(n, -1) == n:
                return n
            val = trace(union.get(n, -1))
            #union[n] = val
            return val
        zeros_s = sorted(zeros)
        while zeros:
            res.append(mx)
            idx = zeros.pop()
            left_idx = bisect.bisect(zeros_s, idx) - 2
            if left_idx in union and sums[left_idx] > 0:
                left_val = sums[trace(left_idx)]
            else:
                left_val = 0
            right_idx = bisect.bisect(zeros_s, idx)
            if right_idx in union and sums[right_idx] > 0:
                right_val = sums[trace(right_idx)]
            else:
                right_val = 0

            

            left_seg = pre[idx+1] - pre[max(left_idx, 0)]
            right_seg = pre[min(right_idx+1, len(pre) - 1)] - pre[idx]
            val = nums[idx]

            s = left_val + right_val + left_seg + right_seg + val
            mx = max(mx, s)
            if right_idx in union and sums[right_idx] > 0:
                merge(idx, right_idx)
            if left_idx in union and sums[left_idx] > 0:
                merge(idx, left_idx)

            sums[idx] = s

       
        res.reverse()
        return res
