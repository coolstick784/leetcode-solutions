class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        needs = needs + [0 for _ in range(len(needs), 6)]
        new_specials = []
        for idx, p in enumerate(price):
            new_specials.append([0 for _ in range(idx)] + [1] + [0 for _ in range(idx+1, 6)] + [p])

        for s in special:
            normal_cost = sum(s[i] * price[i] for i in range(len(price)))
            if s[-1] < normal_cost:
                new_specials.append(s[:-1] + [0 for _ in range(len(s)-1, 6)] + [s[-1]])
        
        specials = new_specials.copy()


        @lru_cache(None)
        def lowest(n1, n2, n3, n4, n5, n6):
   
            if n1==0 and n2 ==0 and n3==0 and n4==0 and n5==0 and n6==0:
                return 0
            if n1 <0 or n2 <0 or n3<0 or n4<0 or n5<0 or n6<0:
                return float('inf')
            out = []
            for s in specials:
                if n1<s[0] or n2<s[1] or n3<s[2] or n4<s[3] or n5<s[4] or n6<s[5]:
                    continue
                out.append(s[-1] + lowest(n1-s[0], n2-s[1], n3-s[2], n4-s[3], n5-s[4], n6-s[5]))


            return min(out)



        return lowest(needs[0], needs[1], needs[2], needs[3], needs[4], needs[5])
