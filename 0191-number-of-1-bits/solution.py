pows = [1]
for n in range(31):
    pows.append(2*pows[-1])
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        cur = n
        left_idx = len(pows) - 1
        while cur > 0:
            if cur >= pows[left_idx]:
                total += 1
                cur -= pows[left_idx]
            
            left_idx -= 1
        return total
