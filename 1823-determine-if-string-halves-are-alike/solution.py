class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
        ctr_a = Counter(a)
        ctr_b = Counter(b)
        return sum([ctr_a[v] for v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) ==  sum([ctr_b[v] for v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) 
