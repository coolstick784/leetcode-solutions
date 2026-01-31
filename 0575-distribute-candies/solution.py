class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        len_c = int(len(candyType) / 2)
        unique = set()
        for n in candyType:
            unique.add(n)
            if len(unique) >= len_c:
                return len_c
        return int(len(unique))


        
