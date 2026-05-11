# for each section 1-11, bob either hits 1 more than alice or 0
# fill the rest in with scoring section 0

# so we have 11 bits, 1-11, so we can go up to 2^12-1
# for each number, convert it to a bit, and see if it's feasble
# if it is, the sum of idxs is our score
pows = [1]
for _ in range(10):
    pows.append(2*pows[-1])
binary = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
m = 2**12
def convertBinary(n):
    out = []
    for p in pows:
        if n & p:
            out.append(1)
        else:
            out.append(0)
    out.reverse()
    return out
for n in range(m):
    binary.append(convertBinary(n))
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        need = []
        for n in aliceArrows:
            need.append(n+1)
        res = 0
        
        def isPossible(cur_binary):
            cur = numArrows
            out = 0
            for i in range(1, 12):
                if cur_binary[i-1]:
                    cur -= need[i]
                    out += i
                if cur < 0:
                    return [0, 0]
            return [cur, out]
            


        final = [numArrows] + [0 for _ in range(10)]
        for n in range(1, m):
            cur_binary = binary[n]
            left, score = isPossible(cur_binary)
            if score > res:
                res = score
                final = [left]
      
                for idx, pos in enumerate(cur_binary):
                    if pos:
                        final.append(need[idx+1])

                    else:
                        final.append(0)


        return final
