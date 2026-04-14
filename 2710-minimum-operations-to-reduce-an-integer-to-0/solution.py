# the answer for 10 will be the same as -10
#  basically, we want to get the distance between the 2 values closest to n in the list of powers of 2
# then, our answer is 1 + the min ops of that distance and so on



pows_2 = [1]
for _ in range(20):
    pows_2.append(2*pows_2[-1])
class Solution:
    def minOperations(self, n: int) -> int:
      
        if n in pows_2:
            return 1
        right_idx = bisect.bisect_left(pows_2, n)
        left_idx = right_idx-1
     
        return min(1+self.minOperations(abs(n-pows_2[left_idx])), 1+self.minOperations(abs(n-pows_2[right_idx])))

