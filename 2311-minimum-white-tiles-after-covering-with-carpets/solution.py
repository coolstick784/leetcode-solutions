class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        best = {} # (number of carpets, starting point)
        sums = [0]

        for idx, ch in enumerate(floor):
            
            if ch == '1':
                sums.append(sums[-1] + 1)
            else:
                sums.append(sums[-1])
        # to get from idx 0 to idx 2 inclusive, we do sums[3] - sums[0]

        for idx in range(len(floor) -1, -1, -1):
            for n in range(numCarpets+1):
                best[(n, idx)] = best.get((n, idx+1), 0) + sums[idx+1] - sums[idx]# dont add one here

                
                if n > 0:
                    best[(n, idx)] = min(best[(n, idx)], best.get((n-1, idx+carpetLen), 0))
         
        return best[(numCarpets, 0)]
