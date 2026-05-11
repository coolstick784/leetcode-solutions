class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a,b,c]
        stones.sort()

        def findLowest(s1, s2, s3):
            if s1 == s2-1 and s3 == s2+1:
                return 0
            if s1 == s2-1 or s3==s2+1:
                return 1
            if s2 == s1+2 or s2 == s3-2:
                return 1
            return 2


        def findHighest(s1, s2, s3):
            return (s2-s1) -1 + (s3-s2) -1

        return [findLowest(stones[0], stones[1], stones[2]), findHighest(stones[0], stones[1], stones[2])]
