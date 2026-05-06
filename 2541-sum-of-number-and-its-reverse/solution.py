sums = set()
def reverse(n):
    revd = list(str(n))
    revd.reverse()
    revd = int("".join(revd))
    return n + revd
for n in range(10**5+1):
    sums.add(reverse(n))


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num in sums:
            return True
        return False
        
