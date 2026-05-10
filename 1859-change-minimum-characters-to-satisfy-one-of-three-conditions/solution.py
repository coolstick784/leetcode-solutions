# so get the min of each possibility? seems easy enough

letters = [chr(ord('a') + n) for n in range(26)]
class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        def makeOne(s):
            out = len(s)
            ctr = Counter(s)
            for letter in letters:

                out = min(out, len(s) - ctr.get(letter,0))
            return out

        # for each letter, calculate the amount of steps it would take to get every letter in s1 <= that and every letter in s2 > that
        def makeLess(s1, s2):
            ctr1 = Counter(s1)
            ctr2 = Counter(s2)
            cur1 = len(s1)
            cur2 = 0
            out = float('inf')
            for idx, letter in enumerate(letters[:-1]):
                
                cur1 -= ctr1[letter]
                cur2 += ctr2[letter]
                out = min(out, cur1+cur2)
            return out
                




            
        three = makeOne(a) + makeOne(b)
        two = makeLess(b, a)
        one = makeLess(a, b)
        return min([three, one, two])
        
