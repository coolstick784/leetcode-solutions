class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        verticalCut.reverse()
        res = 0
        hl = len(horizontalCut)
        h_sum = sum(horizontalCut)
        h_idx = len(horizontalCut) - 1
        res += h_sum
        res += sum(verticalCut)
        n_vert = 0
        print(verticalCut)
        print(horizontalCut)
        
        for idx, num in enumerate(verticalCut):
            #print("idx", idx, "start", res)
            while h_idx >= 0 and horizontalCut[h_idx] >= num:
                h_sum -= horizontalCut[h_idx]
                h_idx -= 1
                
                n_vert += 1
            res += (h_sum + num * n_vert)

        return res
            
        

