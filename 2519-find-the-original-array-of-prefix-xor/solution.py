#[5, 2, 0, 3, 1]
#[5] cur = 5 -> next is 5^2 = 7
#[5, 7] cur = cur^7 = 2 -> next is 2^0 = 2
#[5, 7, 2] cur=cur^2 = 0 -> next is 0^3 = 3
#[5, 7, 2, 3] cur = cur^3=3 -> next is 3^1=2
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        cur = 0
        res = []
        for p in pref:
            next_val = cur ^ p
            cur = cur^next_val
            res.append(next_val)
        return res

