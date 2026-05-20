class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        dups = set()

        res = []
        for idx in range(len(A)):
            a = A[idx]
            b = B[idx]
            set_a.add(a)
            set_b.add(b)
            if a in set_b:
                dups.add(a)
            if b in set_a:
                dups.add(b)
            res.append(len(dups))
        return res

